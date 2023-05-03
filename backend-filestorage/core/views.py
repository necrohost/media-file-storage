import socket
import uuid

from django.contrib.auth.models import User
from django.http import FileResponse
from rest_framework import permissions, viewsets, generics
from rest_framework.decorators import action
from rest_framework.fields import CurrentUserDefault
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import File
from .permissions import IsOwner
from .serializers import FileSerializer, UserSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True)
    def whoami(self, request):
        hostname = socket.getfqdn()
        ip = socket.gethostbyname_ex(hostname)[2][0]
        return Response({"id": self.request.user.id,
                         "username": self.request.user.username,
                         "email": self.request.user.email,
                         "local ip": ip
                         })


class FileSharedViewSet(viewsets.ModelViewSet):
    pass


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all().order_by('-upload_at')
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        owner_id = self.request.user.id
        queryset = File.objects.filter(owner_id=owner_id)
        return queryset

    @action(methods=['get'], detail=True)
    def download(self, request, pk):
        file = File.objects.get(id=pk)
        file_handle = file.file.open()
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = file.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % file.file.name

        return response

    @action(detail=True)
    def share(self, request, *args, **kwargs):
        file = self.get_object()
        file.shared_link = uuid.uuid4().hex
        file.save()
        return Response(file.shared_link)

    @action(detail=False)
    def shared(self, request):
        shared_files = File.objects.exclude(shared_link__isnull=True).exclude(shared_link__exact='')

        page = self.paginate_queryset(shared_files)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(shared_files, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def shared_file(self, request, *args, **kwargs):
        link = kwargs['uuid']
        shared_file = File.objects.get(shared_link=link)
        file_handle = shared_file.file.open()
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = shared_file.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % shared_file.file.name

        return response

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
