from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("secret", views.secret, name="secret"),
    path('api-token-auth/', obtain_auth_token),
]
