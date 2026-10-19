"""Роутер"""
from request import Request
from response import Response

from constants import _404

class Router:
    """Хранит маршруты и вызывает нужный метод контроллера."""

    def __init__(self):
        """Создаёт пустую таблицу маршрутов."""
        self.routes = []

    def register(self, controller_class):
        """Регистрирует все методы контроллера, помеченные @route.

        controller_class - класс контроллера."""

        for attr_name in dir(controller_class):
            method = getattr(controller_class, attr_name)

            if not hasattr(method, "_route_path"):
                continue

            path = method._route_path
            http_method = method._route_method

            self.routes.append((path, http_method, controller_class, attr_name))
            print(f"[route] {http_method:6} {path} -> {controller_class.__name__}.{attr_name}")

    def register_all(self):
        """Регистрирует все контроллеры приложения."""
        from controllers.home_controller import HomeController

        self.register(HomeController)

    def handle(self, environ, start_response):
        """Обрабатывает запрос: находит маршрут и вызывает контроллер.

        environ - словарь.
        start_response - функция, которой отдаём статус и заголовки.
        Возвращает список байтов.
        """
        request = Request(environ)

        # Пробегаем по таблице маршрутов и ищем подходящий.
        for path, http_method, controller_class, action_name in self.routes:
            if path == request.path and http_method == request.method:
                controller = controller_class(request)

                action = getattr(controller, action_name)
                response = action()

                if not isinstance(response, Response):
                    response = Response(body=str(response))

                return response.to_wsgi(start_response)

        response = Response(body="<h1>404 — Страница не найдена</h1>",
                            status=_404)
        return response.to_wsgi(start_response)