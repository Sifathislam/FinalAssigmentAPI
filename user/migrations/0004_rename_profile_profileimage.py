# Generated by Django 4.2.7 on 2024-01-14 18:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileImage',
        ),
    ]
