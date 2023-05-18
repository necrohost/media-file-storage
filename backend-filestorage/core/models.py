import os

from django.db import models
from django.utils import timezone


class File(models.Model):
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)
    name = models.CharField("name", max_length=50)
    file = models.FileField("file", max_length=100)
    size = models.FloatField("size")
    ext = models.CharField("extension", max_length=50, default='', blank=True)
    shared_link = models.CharField(max_length=50, blank=True)
    encrypted = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete()

    def soft_delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = self.file.name
            self.size = self.file.size
            self.ext = os.path.splitext(self.file.name)[1].lower()
        super().save(*args, **kwargs)
