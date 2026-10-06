import json

from response import Response

class BaseController:
    """Базовый контроллер."""

    def __init__(self, request): 
        """Сохраняет объект запроса, чтобы наследники могли его использовать.
        
        request - объект класса Request с данными текущего запроса.
        """

        self.request = request

    def html(self, body, status = "200 OK"):
        """Возврашает html-ответ
        
        body - html строка.
        status - статус ответа. По умолчанию 200.
        """

        return Response(body=body, status=status)

    def json(self, data, status = "200 OK"):
        """Возвращает json-ответ
        
        data - любой объект, который будет превращен в json.

        status - статус ответа. По умолчанию 200.
        """

        body = json.dumps(data, ensure_ascii=False)

        return Response(body = body, status = status, content_type="application/json; charset=utf-8")

