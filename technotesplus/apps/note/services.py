import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


logger = logging.getLogger(__name__)


def send_mail(from_email, to_emails, subject, html_content):
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=html_content,
    )
    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        if response.status_code == 200:
            logger.info(f"Email send successfully to {to_emails}")
    except Exception as e:
        logger.exception(e)


def notify_user_on_note_share(from_email, shared_note):
    try:
        to_emails = shared_note.user.email

        shared_with_user = shared_note.user
        if shared_with_user.name:
            shared_with_user_name = shared_with_user.name
        else:
            shared_with_user_name = shared_with_user.username

        note_user = shared_note.note.user
        if note_user.name:
            note_user_name = note_user.name
        else:
            note_user_name = note_user.username
        subject = f"{note_user_name} has shared a note"

        html_content = f"Hello {shared_with_user_name}, <br><br>{note_user_name} has shared a note with you.<br>Title: {shared_note.title}"

        send_mail(from_email, to_emails, subject, html_content)
    except Exception as e:
        logger.exception(e)
