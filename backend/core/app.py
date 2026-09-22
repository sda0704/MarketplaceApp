# Собирает WSGI-приложение из роутера и обработчиков.
# Единственное место, где встречаются роутер, Response и WSGI.

# Импортирует traceback, чтобы печатать стек ошибок при исключениях в обработчиках.
import traceback

# Импортирует статусы из config.
from config import HTTP_NOT_FOUND, HTTP_INTERNAL_ERROR

# Импортирует Response - с его помощью формируются ответы.
from core.response import Response

# Импортирует Router - с его помощью ищутся обработчики.
from core.router import Router


# Создаёт и возвращает WSGI-приложение, наполняя роутер через переданную функцию.
def create_app(register_routes):
    router = Router()

    register_routes(router)

    # Определяет саму WSGI-функцию, которую будет вызывать сервер.
    def app(environ, start_response):
        method = environ['REQUEST_METHOD']

        path = environ['PATH_INFO']

        handler, params = router.match(method, path)

        if handler is None:
            response = Response('<h1>404 Not Found</h1>', status=HTTP_NOT_FOUND)
        else:
            response = run_handler(handler, environ, params)

        return response(start_response)

    # Возвращает готовое WSGI-приложение.
    return app


# Вызывает обработчик, перехватывая ошибки и превращая их в ответ 500.
def run_handler(handler, environ, params):
    try:
        return handler(environ, **params)

    except Exception as error:
        traceback.print_exc()

        return Response(
            f'<h1>500 Internal Server Error</h1><pre>{error}</pre>',
            status=HTTP_INTERNAL_ERROR,
        )