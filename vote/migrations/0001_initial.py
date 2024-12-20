# Generated by Django 5.1.3 on 2024-11-25 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voting_sessions', '0003_alter_session_choice_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('option', models.CharField(max_length=100)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='voting_sessions.session')),
            ],
        ),
    ]
