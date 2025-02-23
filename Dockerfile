FROM python:3.12-slim

WORKDIR /app

# # Установить зависимости
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Скопировать код при
COPY /.venv

# Запуск приложения
CMD ["python", "main.py"]