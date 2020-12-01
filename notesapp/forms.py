from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from .models import Note


class SignInForm(forms.ModelForm):

    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username",
                "type": "text",
                "id": "username-input",
                "name": "username",
                "class": "username-field form-control",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter password",
                "type": "password",
                "id": "password-input",
                "name": "password",
                "class": "password-field form-control",
            }
        ),
    )

    field_order = [
        "username",
        "password",
    ]

    class Meta:
        model = User
        fields = {
            "username",
            "password",
        }


class NoteForm(forms.ModelForm):

    note_title = forms.CharField(
        label="Title",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter note title",
                "type": "text",
                "id": "note_title-input",
                "name": "Title",
                "class": "note_title-field form-control",
            }
        ),
    )

    note_content = forms.CharField(
        label="Content",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter note content",
                "type": "text",
                "id": "note_content-input",
                "name": "Content",
                "class": "note_content-field form-control",
            }
        ),
    )

    field_order = [
        "note_title",
        "note_content",
    ]

    class Meta:
        model = Note
        fields = {
            "note_title",
            "note_content",
        }