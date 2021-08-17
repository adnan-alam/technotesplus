import uuid
from ckeditor.fields import RichTextField
from slugify import slugify
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(max_length=300, unique=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

    def __str__(self):
        return self.slug

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_id = uuid.uuid4()
        unique_slug = f"{slug}-{unique_id}"
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self._get_unique_slug()
        super(Note, self).save(*args, **kwargs)


class SharedNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "note")
        verbose_name = _("Shared Note")
        verbose_name_plural = _("Shared Notes")

    def __str__(self):
        return f"{self.note} | {self.user}"

    def get_absolute_url(self):
        return ("note", (), {"slug": self.note.slug})
