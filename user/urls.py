from rest_framework import routers
from .views import CustomTokenObtainPairView, RegisterAPI, UserAPI
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', RegisterAPI.as_view(), name='register'),
    path('api/user', UserAPI.as_view(), name='user'),
]
