from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('note_id', 'note_user', 'note_title', 'note_content',
                  'note_created_at', 'note_last_updated_at', 'note_is_archived',)
