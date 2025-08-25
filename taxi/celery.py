import os
from celery import Celery

# Встановлюємо Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("taxi")

# Використовуємо налаштування з Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматично підвантажуємо таски з усіх додатків
app.autodiscover_tasks()
