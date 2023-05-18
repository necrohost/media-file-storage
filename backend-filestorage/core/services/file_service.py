from ..models import File


def get_file(**kwargs):
    return File.objects.get(**kwargs)


def delete_file(**kwargs):
    file_deleted = File.objects.get(**kwargs)
    file_deleted.file.delete()
