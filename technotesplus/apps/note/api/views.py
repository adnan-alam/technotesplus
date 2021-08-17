from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from taggit.models import Tag
from django.contrib.auth import get_user_model
from django.conf import settings
from technotesplus.apps.account.api import permissions as permissions_account
from technotesplus.apps.note import models as models_note
from technotesplus.apps.note import services as services_note
from technotesplus.apps.note.api import serializers as serializers_note


User = get_user_model()


class NoteViewSet(viewsets.ModelViewSet):
    lookup_field = "slug"
    permission_classes = [IsAuthenticated & permissions_account.NotAdminUser]
    serializer_class = serializers_note.NoteSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title", "tags__name"]

    def get_queryset(self):
        queryset = models_note.Note.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SharedNoteViewSet(viewsets.ModelViewSet):
    lookup_field = "note__slug"
    permission_classes = [IsAuthenticated & permissions_account.NotAdminUser]
    serializer_class = serializers_note.SharedNoteSerializer

    def get_queryset(self):
        queryset = models_note.SharedNote.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            shared_note = serializer.save()
            services_note.notify_user_on_note_share(
                settings.DEFAULT_FROM_EMAIL, shared_note
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_viewed:
            instance.is_viewed = True
            instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TagListApiView(ListAPIView):
    permission_classes = [IsAuthenticated & permissions_account.NotAdminUser]
    serializer_class = serializers_note.TagSerializer
    queryset = Tag.objects.all()

    def paginate_queryset(self, queryset):
        if (
            self.paginator
            and self.request.query_params.get(self.paginator.page_query_param, None)
            is None
        ):
            return None
        return super().paginate_queryset(queryset)
