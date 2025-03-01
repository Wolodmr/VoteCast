import os
import logging
from django.core.management.base import BaseCommand
from voting_sessions.utils import send_notifications  

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Adjust based on script depth
LOG_FILE_PATH = os.path.join(BASE_DIR, "email_debug.log")

class Command(BaseCommand):
    help = "Send email notifications for upcoming voting sessions"

    def handle(self, *args, **kwargs):
        logger.info("📢 Running send_notifications command...")
        try:
            send_notifications()
            logger.info("✅ Notifications sent successfully.")
        except Exception as e:
            logger.error(f"❌ Error sending notifications: {e}", exc_info=True)  # Logs full error details
