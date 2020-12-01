from django.db import models
from django.db.models.fields.related import ForeignKey
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class Client(models.Model):
    client_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(blank=False, max_length=512)
    middle_name = models.CharField(blank=True, max_length=512)
    last_name = models.CharField(blank=False, max_length=512)
    phone_number = PhoneNumberField()


class Loan(models.Model):
    loan_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    loan_client = ForeignKey(
        "Client",
        on_delete=models.PROTECT,
    )
    loan_amount = models.PositiveIntegerField(
        blank=False,
        null=True,
    )
    loan_reason = models.TextField(blank=True, null=True)
