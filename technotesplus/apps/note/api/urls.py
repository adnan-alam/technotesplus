from django.urls import path, include
from rest_framework_nested import routers
from technotesplus.apps.note.api import views as views_note


router = routers.DefaultRouter(trailing_slash=True)
router.register(r"notes", views_note.NoteViewSet, basename="note")
router.register(r"shared-notes", views_note.SharedNoteViewSet, basename="shared-note")


urlpatterns = [
    path("", include(router.urls)),
    path("tags/", views_note.TagListApiView.as_view())
]
