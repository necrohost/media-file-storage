import socket
import uuid
import mimetypes

from django.contrib.auth.models import User
from django.http import FileResponse
from django.utils.text import slugify
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import File
from .permissions import IsOwnerOrShared
from .serializers import FileSerializer, UserSerializer, RegisterSerializer
from .services.file_service import get_file


class FileViewSet(viewsets.ModelViewSet):
    # .exclude(is_deleted=True)
    queryset = File.objects.all().order_by('-created_at')
    serializer_class = FileSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self.queryset.filter(owner_id=self.request.user.id)

    @action(methods=['GET'], detail=True, permission_classes=[IsOwnerOrShared])
    def download(self, request, *args, **kwargs):
        download_obj_file = get_file(**kwargs)
        file_handle = download_obj_file.file.open()
        file_mime, _ = mimetypes.guess_type(download_obj_file.file.name)
        response = FileResponse(file_handle,
                                content_type=file_mime,
                                as_attachment=True,
                                filename=download_obj_file.name)
        response['Content-Length'] = download_obj_file.file.size
        return response

    @action(detail=True, methods=['POST'])
    def share(self, request, *args, **kwargs):
        shared_file = self.get_object()
        shared_file.shared_link = uuid.uuid4().hex
        shared_file.save()
        return Response({'link': shared_file.shared_link})

    @action(detail=True, methods=['POST'])
    def set_soft_delete(self, request, *args, **kwargs):
        self.get_object().soft_delete()
        return Response(status=204)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeletedFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.exclude(is_deleted=False).all().order_by('-created_at')
    serializer_class = FileSerializer
    permission_classes = [IsOwnerOrShared]

    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @staticmethod
    def whoami(request):
        hostname = socket.getfqdn()
        ip = socket.gethostbyname_ex(hostname)[2][0]
        return Response({"id": request.user.id,
                         "username": request.user.username,
                         "email": request.user.email,
                         "local ip": ip
                         })
