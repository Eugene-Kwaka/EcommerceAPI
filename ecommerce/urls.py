from django.contrib import admin
from django.urls import path, include
from core.views import *
# I will use two inbuilt views from django_rest_framework for the Login function
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# # token-auth view that connects with a url to create an auth token for a user
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('core.urls')),
    # JWT Registration & Token Login
    path('auth/register/', RegistrationAPIView.as_view(), name="register "),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    ## auth-token url that directs a user to create username and password then dedicate an auth-token
    # path('api/v1/auth/auth-token', obtain_auth_token, name="obtain-auth-token"),
]
