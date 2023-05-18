from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

from .views import FileViewSet, RegisterView, UserViewSet, DeletedFileViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'files', FileViewSet, basename='file')
router.register(r'deleted-files', DeletedFileViewSet, basename='deleted-file')
router.register(r'users', UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),

    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/whoami/', UserViewSet.as_view({'get': 'whoami'}), name='whoami'),

    # path('files/deleted/', DeletedFileViewSet.as_view({'get': 'list'}), name='deleted-files'),
    path('files/<int:pk>/download/', FileViewSet.as_view({'get': 'download'}), name='download-file'),
    path('s/<str:link>', FileViewSet.as_view({'get': 'download'}), name='download-shared-file'),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
