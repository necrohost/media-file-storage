import socket
import uuid

from django.contrib.auth.models import User
from django.http import FileResponse
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
    queryset = File.objects.exclude(is_deleted=True).all().order_by('-created_at')
    serializer_class = FileSerializer
    permission_classes = [IsOwnerOrShared]

    authentication_classes = [JWTAuthentication, TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        return self.queryset.filter(owner_id=self.request.user.id)

    @action(methods=['get'], detail=True)
    def download(self, request, *args, **kwargs):
        download_obj_file = get_file(**kwargs)
        file_handle = download_obj_file.file.open()
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = download_obj_file.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % download_obj_file.file.name
        return response

    @action(detail=True, methods=['POST'])
    def share(self, request, *args, **kwargs):
        shared_file = self.get_object()
        shared_file.shared_link = uuid.uuid4().hex
        shared_file.save()
        return Response(shared_file.shared_link)

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
