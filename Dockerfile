FROM python:3.12-slim

WORKDIR /app

# Скопировать зависимости и установить их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать код приложения
COPY main.py .

# Запуск приложения
CMD ["python", "main.py"]
