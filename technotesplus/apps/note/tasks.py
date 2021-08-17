import logging
from huey import crontab
from huey.contrib.djhuey import periodic_task
from django.conf import settings
from technotesplus.apps.note import models as models_note
from technotesplus.apps.note import services as services_note


logger = logging.getLogger(__name__)


@periodic_task(crontab(minute=0, hour=12, day="*/1"))
def task_notify_user():
    try:
        logger.info("[task_notify_user] Executing ...")

        from_email = settings.DEFAULT_FROM_EMAIL
        shared_notes_not_viewed = models_note.SharedNote.objects.filter(is_viewed=False)
        for shared_note in shared_notes_not_viewed:
            services_note.notify_user_on_note_share(from_email, shared_note)

        logger.info("[task_notify_user] Executed - Successful")
    except Exception as e:
        logger.exception(e)
        logger.info("[task_notify_user] Executed - Failed")
