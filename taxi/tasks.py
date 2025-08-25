from celery import shared_task
from django.core.mail import send_mail

# @shared_task
# def test_task():
#     print("Hello Celery! 🚀")
#     return "Task completed"


@shared_task
def send_welcome_email(email, username):
    subject = "Вітаємо у Taxi Service!"
    message = f"Привіт, {username}! Дякуємо за реєстрацію у нашому сервісі."
    from_email = "taxi@example.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
