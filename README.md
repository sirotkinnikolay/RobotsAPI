## Запуск контейне:
- В директории где находится файл docker-compose.yaml.

Cоздать и запустить  контейнер с помощью команды: ``docker-compose up --build``
## Устаановка ``curl``
- ``sudo apt update``
- ``sudo apt install curl``

## Получение токена доступа OAuth2:
- зарегистрировать приложение по адресу: http://localhost:8000/o/applications/
- получить токен доступа: ``curl -X POST "http://localhost:8000/o/token/" -d "grant_type=password&username=<YOUR_USERNAME>&password=<YOUR_PASSWORD>&client_id=<CLIENT_ID>&client_secret=<CLIENT_SECRET>"``

