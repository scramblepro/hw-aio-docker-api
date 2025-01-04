FROM python:3.12-slim

WORKDIR /app

# # Установить зависимости
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Скопировать код приложения
COPY . .

# Запуск приложения
CMD ["python", "app.py"]
