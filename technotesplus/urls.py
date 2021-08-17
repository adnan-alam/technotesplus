"""technotesplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path("", include("technotesplus.apps.core.urls")),
    path("account/", include("technotesplus.apps.account.urls")),
    path("admin/", admin.site.urls),
    path("notes/", include("technotesplus.apps.note.urls")),
    # jwt
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # api endpoints
    path("api/v1/account/", include("technotesplus.apps.account.api.urls")),
    path("api/v1/n/", include("technotesplus.apps.note.api.urls")),
]
