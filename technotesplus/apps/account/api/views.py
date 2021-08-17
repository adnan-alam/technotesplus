from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from technotesplus.apps.account.api import serializers as serializers_account
from technotesplus.apps.account.api import permissions as permissions_account


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action == "create":
            permission_classes = [AllowAny]
        elif self.action == "destroy":
            permission_classes = [IsAuthenticated & IsAdminUser]
        else:
            permission_classes = [IsAuthenticated & permissions_account.NotAdminUser]

        return [permission() for permission in permission_classes]

    serializer_class = serializers_account.UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = TokenObtainPairSerializer.get_token(user)
            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
