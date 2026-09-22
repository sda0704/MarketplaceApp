# Импортирует Response, чтобы обработчики могли возвращать ответ.
from core.response import Response


# Регистрирует все маршруты этого модуля на переданном роутере.
def register(router):
    # Регистрирует обработчик главной страницы.
    @router.route('GET', '/')
    def home(environ):
        return Response('<h1>Marketplace</h1><p>Главная</p>')

    # Регистрирует обработчик страницы "О проекте".
    @router.route('GET', '/about')
    def about(environ):
        # Возвращает простую HTML-страницу "О проекте".
        return Response('<h1>О проекте</h1>')

    # Регистрирует обработчик страницы товара с параметром pid.
    @router.route('GET', '/product/<pid>')
    def product(environ, pid):
        # Возвращает HTML-страницу с подставленным идентификатором товара.
        return Response(f'<h1>Товар #{pid}</h1>')