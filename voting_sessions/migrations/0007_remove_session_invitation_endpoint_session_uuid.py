# Generated by Django 5.1.5 on 2025-03-14 17:35

from django.db import migrations, models
import uuid

def generate_unique_uuids(apps, schema_editor):
    Session = apps.get_model("voting_sessions", "Session")
    for session in Session.objects.all():
        session.uuid = uuid.uuid4()
        session.save(update_fields=["uuid"])

class Migration(migrations.Migration):

    dependencies = [
        ("voting_sessions", "0006_alter_session_creator_email_and_more"),  # Update with your last migration
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="uuid",
            field=models.UUIDField(null=True),  # Temporarily allow NULL
        ),
        migrations.RunPython(generate_unique_uuids, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name="session",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True, editable=False),
        ),
    ]

