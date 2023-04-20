from django.contrib.auth.models import User
from rest_framework import serializers

from .models import File


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'files']


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['url', 'name', 'size', 'file', 'ext', 'upload_at', 'shared_link', 'encrypted', 'owner']
        read_only_fields = ['url', 'name', 'size', 'ext', 'upload_at', 'owner']
