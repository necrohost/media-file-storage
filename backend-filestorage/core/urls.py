from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'files', views.FileViewSet, basename='file')
router.register(r'users', views.UserViewSet, basename='user')

shared_file_detail = views.FileViewSet.as_view({'get': 'shared_file'})

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('s/<str:uuid>', shared_file_detail, name='shared-file-detail'),
]
