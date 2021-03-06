# Generated by Django 3.1.4 on 2020-12-01 03:25

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=512)),
                ('middle_name', models.CharField(blank=True, max_length=512)),
                ('last_name', models.CharField(max_length=512)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('loan_amount', models.PositiveIntegerField(null=True)),
                ('loan_reason', models.TextField(blank=True, null=True)),
                ('loan_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shree_finance.client')),
            ],
        ),
    ]
