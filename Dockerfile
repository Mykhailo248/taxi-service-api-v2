# Базовий образ Python
FROM python:3.12-slim

# Змінні середовища
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Робоча директорія в контейнері
WORKDIR /app

# Встановлюємо системні пакети
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Копіюємо залежності
COPY requirements.txt /app/

# Встановлюємо Python-залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код проєкту
COPY . /app/

# Копіюємо entrypoint і робимо його виконуваним
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Точка запуску контейнера
ENTRYPOINT ["/app/entrypoint.sh"]
