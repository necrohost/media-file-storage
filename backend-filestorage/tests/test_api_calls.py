import json
import os
import re

import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework_simplejwt.tokens import AccessToken


@pytest.fixture()
def no_auth_client():
    return APIClient()


@pytest.fixture()
def auth_token_client():

    user = User.objects.create_user(username='example3', password='example3333', email='example3@mail.com')
    user.save()
    user_data = {"username": "example3", "password": "example3333"}
    client = APIClient()
    response = client.post('/api/auth/login/', user_data, format='json')
    content = json.loads(response.content)
    token = content['access']

    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    return client


@pytest.fixture(autouse=True)
def file_upload_payload():
    upload_file = SimpleUploadedFile('test_file.txt', b'yes_this_test', content_type="text/plain")
    return {"file": upload_file}


@pytest.fixture
def teardown_for_testing_files():
    yield
    print("\nDeleting test files...")
    for f in os.listdir('cloud'):
        if re.search('test_file', f):
            os.remove(os.path.join('cloud', f))
    print("\nDeleted test files")


class TestAuth:
    @pytest.mark.django_db
    def test_register_user(self, no_auth_client):
        user = {"email": "something@mail.com",
                "username": "someone",
                "password": "something123"
                }
        response = no_auth_client.post('/api/auth/register/', user, format='json')
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_login_valid_user(self, no_auth_client, django_user_model):
        user = django_user_model.objects.create(email="example2@mail.com",
                                                username="example2",
                                                password="example222",
                                                )
        user.save()
        user_data = {"username": "example2", "password": "example222"}
        if user.clean():
            response = no_auth_client.post('/api/auth/login/', user_data, format='json')
            content = json.loads(response.content)

            assert response.status_code == status.HTTP_200_OK
            assert content['access']

    @pytest.mark.django_db
    def test_get_list_of_users(self, auth_token_client):
        response = auth_token_client.get('/api/users/', format='json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_get_info_user(self, auth_token_client):
        response = auth_token_client.get('/api/auth/whoami/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_get_user(self, auth_token_client):
        user_obj = AccessToken(auth_token_client._credentials['HTTP_AUTHORIZATION'].replace('Bearer ', ''))
        user_id = user_obj['user_id']
        response = auth_token_client.get(f'/api/users/{user_id}/')
        assert response.status_code == status.HTTP_200_OK


class TestFiles:
    @pytest.mark.django_db
    def test_get_list_of_files(self, auth_token_client):
        response = auth_token_client.get('/api/files/', format='json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_get_file(self, auth_token_client, file_upload_payload):
        response = auth_token_client.post('/api/files/', file_upload_payload, format='multipart')
        decode_res = json.loads(response.content)
        decode_id = decode_res['id']
        response = auth_token_client.get(f'/api/files/{decode_id}/', format='json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_get_list_of_deleted_files(self, auth_token_client):
        response = auth_token_client.get('/api/deleted-files/', format='json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_upload_file(self, auth_token_client, file_upload_payload):
        response = auth_token_client.post('/api/files/', file_upload_payload, format="multipart")
        assert response.status_code == status.HTTP_201_CREATED, 'Not created file'

    @pytest.mark.django_db
    def test_download_file(self, auth_token_client, file_upload_payload):
        response = auth_token_client.post('/api/files/', file_upload_payload, format="multipart")
        decode_res = json.loads(response.content)
        decode_id = decode_res['id']
        response = auth_token_client.get(f'/api/files/{decode_id}/')
        assert response.status_code == status.HTTP_200_OK, 'No download'

    @pytest.mark.django_db
    def test_hard_delete_file(self, auth_token_client, file_upload_payload):
        response = auth_token_client.post('/api/files/', file_upload_payload, format="multipart")
        decode_res = json.loads(response.content)
        decode_id = decode_res['id']
        response = auth_token_client.delete(f'/api/files/{decode_id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT, 'Not hard deleted file'

    @pytest.mark.django_db
    def test_soft_delete_file(self, auth_token_client, file_upload_payload):
        response = auth_token_client.post('/api/files/', file_upload_payload, format="multipart")
        decode_res = json.loads(response.content)
        decode_id = decode_res['id']
        response = auth_token_client.post(f'/api/files/{decode_id}/set_soft_delete/')
        assert response.status_code == status.HTTP_204_NO_CONTENT, 'Not set soft delete'

    @pytest.mark.django_db
    def test_download_shared_file(self, auth_token_client, no_auth_client, file_upload_payload, teardown_for_testing_files):
        response = auth_token_client.post('/api/files/', file_upload_payload, format="multipart")
        decode_res = json.loads(response.content)
        decode_id = decode_res['id']
        shared_link_json = auth_token_client.post(f'/api/files/{decode_id}/share/', format="json")
        shared_link_decoded = json.loads(shared_link_json.content)
        response = no_auth_client.get('/s/' + str(shared_link_decoded['link']), format="json")
        assert response.status_code == status.HTTP_200_OK
