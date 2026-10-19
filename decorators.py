"""Декораторы для маршрутизации"""

def  route(path, method="GET"):
    """Декоратор. Прикрепляет к функции HTTP-метод
    
    path - строка с путем.
    method - HTTP-метод. По умолчанию GET.
    """

    def wrapper(func):
        """Внутренняя функция, которая получает декорируемую функцию."""

        func._route_path = path
        func._route_method = method.upper()

        return func

    return wrapper

