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
                "class": "note_title-field w-full bg-white rounded border border-gray-300 focus:border-teal-500 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out",
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
                "class": "note_content-field w-full bg-white rounded border border-gray-300 focus:border-teal-500 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out",
            }
        ),
    )

    note_is_archived = forms.BooleanField(
        label="Archive",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "id": "note_is_archived-input",
                "type": "checkbox",
                "name": "Archive",
                "class": "note_is_archived-field w-4 bg-white border text-gray-700 focus:border-teal-500 border-gray-300 text-base outline-none rounded py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out",
            }
        ),
    )

    field_order = [
        "note_title",
        "note_content",
        "note_is_archived",
    ]

    class Meta:
        model = Note
        fields = {
            "note_title",
            "note_content",
            "note_is_archived",
        }