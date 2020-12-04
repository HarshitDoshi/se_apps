from django.db import models
from django.contrib.auth.models import User
import uuid


class Note(models.Model):
    note_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    note_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    note_title = models.CharField(
        verbose_name="Title",
        max_length=1024,
        blank=True,
        null=True,
    )
    note_content = models.TextField(
        verbose_name="Content",
        blank=False,
        null=True,
    )
    note_created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Note created date/time",
    )
    note_last_updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Note last updated date/time",
    )
    note_is_archived = models.BooleanField(
        default=False,
        verbose_name="Archive",
    )

    def __str__(self):
        return self.note_title
