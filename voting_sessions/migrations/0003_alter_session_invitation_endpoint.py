# Generated by Django 5.1.5 on 2025-02-28 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_sessions', '0002_alter_session_choice_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='invitation_endpoint',
            field=models.URLField(blank=True, default='https://example.comm', max_length=500, null=True),
        ),
    ]
