# Generated by Django 3.2.5 on 2023-03-14 14:08

import base.models.order_models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=base.models.order_models.custom_timestamp_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('uid', models.CharField(editable=False, max_length=50)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('tax_included', models.PositiveIntegerField(default=0)),
                ('items', models.JSONField()),
                ('shipping', models.JSONField()),
                ('shipped_at', models.DateTimeField(blank=True, null=True)),
                ('canceled_at', models.DateTimeField(blank=True, null=True)),
                ('memo', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
