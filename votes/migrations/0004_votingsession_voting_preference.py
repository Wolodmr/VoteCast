# Generated by Django 5.0.7 on 2024-10-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_delete_libraryoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingsession',
            name='voting_preference',
            field=models.CharField(choices=[('open', 'Open voting'), ('closed', 'Closed voting')], default='open', max_length=6),
        ),
    ]