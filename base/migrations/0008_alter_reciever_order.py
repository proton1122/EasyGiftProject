# Generated by Django 3.2.5 on 2023-03-25 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_onetoonefield_reciever_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciever',
            name='Order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.order'),
        ),
    ]
