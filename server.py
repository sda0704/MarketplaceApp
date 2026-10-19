from wsgiref.simple_server import make_server

from router import Router

router = Router()
router.register_all()

def app(environ, start_response):
    """Главная функция. Вызывается на каждый http-запрос.
    
    environ - словарь со всеми данными запроса.
    start-response - функция, которой передается статус и заголовки.

    Возвращает список байтов - тело ответа.
    """

    return router.handle(environ, start_response)
    
if __name__ == "__main__":
    """Выполняется при запуске файла."""

    with make_server("localhost", 8000, app) as httpd:
        print("Сервер запущен: http://localhost:8000")
        httpd.serve_forever()