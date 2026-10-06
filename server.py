from wsgiref.simple_server import make_server
from response import Response
from request import Request

def app(environ, start_response):
    """Главная функция. Вызывается на каждый http-запрос.
    
    environ - словарь со всеми данными запроса.
    start-response - функция, которой передается статус и заголовки.

    Возвращает список байтов - тело ответа.
    """
    request = Request(environ)


    if request.path == "/":
        response = Response(body="<h1>Главная страница</h1><a href='/about'>О нас</a>")
    elif request.path == "/about":
        response = Response(body="<h1>О нас</h1><p>Мы продаём всё.</p><a href='/'>На главную</a>")
    else:
        response = Response(body="<h1>Страница не найдена</h1>", status="404 Not Found")

    # print(request.query)

    return response.to_wsgi(start_response)
    
if __name__ == "__main__":
    """Выполняется при запуске файла."""

    with make_server("localhost", 8000, app) as httpd:
        print("Сервер запущен: http://localhost:8000")
        httpd.serve_forever()