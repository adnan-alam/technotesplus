from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from taggit.models import Tag
from rest_framework import serializers
from django.contrib.auth import get_user_model
from technotesplus.apps.core.api.serializers import DynamicFieldsModelSerializer
from technotesplus.apps.note import models as models_note


User = get_user_model()


class NoteSerializer(TaggitSerializer, DynamicFieldsModelSerializer):
    slug = serializers.SlugField(required=False)
    tags = TagListSerializerField()

    class Meta:
        model = models_note.Note
        fields = ["id", "title", "content", "slug", "tags", "created_at", "modified_at"]

    def create(self, validated_data):
        request = self.context["request"]
        tags = validated_data.pop("tags")
        note = models_note.Note.objects.create(user=request.user, **validated_data)
        note.tags.add(*tags)
        return note


class SharedNoteSerializer(DynamicFieldsModelSerializer):
    note_slug = serializers.SlugField(source="note.slug")

    class Meta:
        model = models_note.SharedNote
        fields = ["id", "user", "note", "note_slug", "is_viewed", "created_at"]


class TagSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
