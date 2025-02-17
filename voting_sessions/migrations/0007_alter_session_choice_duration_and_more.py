# Generated by Django 5.1.5 on 2025-02-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting_sessions', '0006_session_session_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='choice_duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='voting_duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
