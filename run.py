# Импортирует os для работы с путями.
import os

# Импортирует sys, чтобы добавить каталог backend в путь поиска модулей.
import sys

# Добавляет каталог backend в sys.path - так работают импорты config, core, routes.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Импортирует стандартный WSGI-сервер из библиотеки Python.
from wsgiref.simple_server import make_server

# Импортирует настройки хоста и порта.
from config import HOST, PORT

# Импортирует фабрику WSGI-приложения.
from core.app import create_app

# Импортирует функцию регистрации маршрутов страниц.
from routes.pages import register as register_pages


# Создаёт приложение и запускает сервер на постоянное прослушивание.
def main():
    app = create_app(register_pages)

    # Создаёт и запускает сервер, слушающий указанный хост и порт.
    with make_server(HOST, PORT, app) as httpd:
        print(f'Сервер запущен: http://{HOST}:{PORT}')

        httpd.serve_forever()

if __name__ == '__main__':
    main()