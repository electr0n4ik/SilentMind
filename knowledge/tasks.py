import os

from celery import shared_task
from django.core.mail import send_mail
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)
# celery -A your_project_name worker --loglevel=info


@shared_task
def send_update_notification(email, course_name):
    subject = 'Уведомление об обновлении курса'
    message = f'Курс "{course_name}" был обновлен. Проверьте новый материал!'
    from_email = os.getenv('EMAIL_HOST_USER')
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
