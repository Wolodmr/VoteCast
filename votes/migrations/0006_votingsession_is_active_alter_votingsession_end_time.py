# Generated by Django 5.0.7 on 2024-10-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_votingsession_open_votes_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingsession',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='votingsession',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]