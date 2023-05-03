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

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('whoami/', views.UserViewSet.as_view({'get': 'whoami'}), name='whoami'),

    path('files/<int:pk>/download/', views.FileViewSet.as_view({'get': 'download'})),
    path('s/<str:uuid>', views.FileViewSet.as_view({'get': 'shared_file'}), name='shared-file-detail'),
]
