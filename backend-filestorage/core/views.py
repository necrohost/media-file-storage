import uuid

from django.contrib.auth.models import User
from django.http import FileResponse
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all().order_by('-upload_at')
    serializer_class = FileSerializer
    # permission_classes = [permissions.IsAuthenticated]

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
