from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Client


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


class ClientForm(forms.ModelForm):

    first_name = forms.CharField(
        label="First name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "(max 512 characters)",
                "type": "text",
                "id": "first_name-input",
                "name": "first_name",
                "class": "first_name-field form-control",
            }
        ),
    )

    middle_name = forms.CharField(
        label="Middle name",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "(optional) (max 512 characters)",
                "type": "text",
                "id": "middle_name-input",
                "name": "middle_name",
                "class": "middle_name-field form-control",
            }
        ),
    )

    last_name = forms.CharField(
        label="Last name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "(max 512 characters)",
                "type": "text",
                "id": "last_name-input",
                "name": "last_name",
                "class": "last_name-field form-control",
            }
        ),
    )

    phone_number = PhoneNumberField(
        label="Phone number",
        required=True,
        widget=PhoneNumberPrefixWidget(
            attrs={
                "placeholder": "10-digit phone number",
                "id": "phone_number-input",
                "name": "phone_number",
                "class": "phone_number-field form-control",
            }
        ),
    )

    field_order = [
        "first_name",
        "middle_name",
        "last_name",
        "phone_number",
    ]

    class Meta:
        model = Client
        fields = {
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
        }