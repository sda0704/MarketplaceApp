from urllib.parse import parse_qs

class Request:
    """Хранит данные запроса: метод, путь и query-параметры"""

    def __init__(self, environ):
        """Достает данные из environ и сохраняет в объект"""

        self.environ = environ
        self.method = environ.get("REQUEST_METHOD", "GET")
        self.path = environ.get("PATH_INFO", "/")

        # Получение данных после "?"
        query_string = environ.get("QUERY_STRING", "")

        # Превращение значения после "?" в словарь
        self.query = parse_qs(query_string)

    def get(self, key, default=None):
        """Возвращает первый query-параметр по имени"""

        values = self.query.get(key)

        if values: 
            return values[0]

        return default