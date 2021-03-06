from django.urls import path, include
from rest_framework_nested import routers
from technotesplus.apps.account.api import views as views_account


router = routers.DefaultRouter(trailing_slash=True)
router.register(r"users", views_account.UserViewSet, basename="user")

urlpatterns = [path("", include(router.urls))]
