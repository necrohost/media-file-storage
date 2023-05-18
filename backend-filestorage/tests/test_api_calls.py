import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib import auth


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def authenticated_api():
    User.objects.create_user(username='example1', password='example1', email='example1@mail.com')
    api = APIClient()
    api.login(username='example1', password='example1')
    return api


@pytest.fixture()
def file_upload_payload():
    upload_file = SimpleUploadedFile('test_file.txt', b'yes_this_test', content_type="text/plain")
    return {"file": upload_file}


class TestAuth:
    @pytest.mark.django_db
    def test_create_user(self, api_client):
        user = {"email": "something@mail.com",
                "username": "someone",
                "password": "something123"
                }
        response = api_client.post('/api/auth/register/', user, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_login_valid_user(self, api_client, django_user_model):
        user = django_user_model.objects.create(email="example2@mail.com",
                                                username="example2",
                                                password="example222",
                                                )
        user.save()
        user_data = {"username": "example2", "password": "example222"}
        if user.clean():
            response = api_client.post('/api/auth/login/', user_data, format='json')
            content = json.loads(response.content)

            assert response.status_code == 200
            assert content['access']

    @pytest.mark.django_db
    def test_get_list_of_users(self, authenticated_api):
        response = authenticated_api.get('/api/users/', format='json')
        assert response.status_code == 200


class TestFiles:
    @pytest.mark.django_db
    def test_get_list_of_files(self, authenticated_api):
        response = authenticated_api.get('/api/files/', format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_list_of_deleted_files(self, authenticated_api):
        response = authenticated_api.get('/api/deleted-files/', format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_upload_file(self, authenticated_api, file_upload_payload):
        response = authenticated_api.post('/api/files/', file_upload_payload, format="multipart")
        assert response.status_code == 201, 'Not created file'

    @pytest.mark.django_db
    def test_download_file(self, authenticated_api, file_upload_payload):
        authenticated_api.post('/api/files/', file_upload_payload, format="multipart")
        response = authenticated_api.get('/api/files/1/download/')
        assert response.status_code == 200, 'Not downloaded'

    @pytest.mark.django_db
    def test_hard_delete_file(self, authenticated_api, file_upload_payload):
        authenticated_api.post('/api/files/', file_upload_payload, format="multipart")
        response = authenticated_api.delete('/api/files/1/')
        assert response.status_code == 204, 'Not hard deleted file'

    # TODO: writing test for: download shared, soft_delete, whoami, file_detail, user_detail
