import os

from django.db import models


class File(models.Model):
    name = models.CharField("name", max_length=50)
    file = models.FileField("file", max_length=100)
    size = models.FloatField("size")
    ext = models.CharField("extension", max_length=50, default='', blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    shared_link = models.CharField(max_length=50, blank=True)
    encrypted = models.BooleanField('encrypted', default=False)
    owner = models.ForeignKey('auth.User', related_name='files', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.name = self.file.name
            self.size = self.file.size
            self.ext = os.path.splitext(self.file.name)[1].lower()
        super().save(*args, **kwargs)
