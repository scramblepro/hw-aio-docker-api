# hw-aio-docker-api

Этот проект представляет собой REST API на AIOHTTP.

Запуск в Docker

# Соберите Docker-образ:

docker build -t hw-aio-docker-api .

# Запустите контейнер:

docker run -d -p 8000:8000 hw-aio-docker-api

Описание API

# Пример запроса к API:

curl http://localhost:8000/