from django.contrib import admin
from django.urls import path, include
# token-auth view that connects with a url to create an auth token for a user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('core.urls')),
    # auth-token url that directs a user to create username and password then dedicate an auth-token
    path('api/v1/auth/auth-token', obtain_auth_token, name="obtain-auth-token"),
]
