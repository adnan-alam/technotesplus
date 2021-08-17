from django.contrib import admin
from technotesplus.apps.note import models as models_note


admin.site.register(models_note.Note)
admin.site.register(models_note.SharedNote)
