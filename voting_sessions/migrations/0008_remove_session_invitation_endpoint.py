# Generated by Django 5.1.5 on 2025-03-14 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_sessions', '0007_remove_session_invitation_endpoint_session_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='invitation_endpoint',
        ),
    ]
