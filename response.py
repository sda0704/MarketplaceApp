"""Обертка htpp-ответа."""

class Response:
    """Представляет HTTP-ответ: статус, заголовки и тело."""

    def __init__(self, body="", status = "200 OK", content_type="text/html; charset=utf-8"):
        """Сохраняет данные ответа.
        
        body - тело ответа.
        status - статус ответа.
        content_type - тип содержимого (по умолчанию HTML в utf-8)
        """

        self.body = body
        self.status = status
        self.content_type = content_type


    def to_wsgi(self, start_response):
        """Отдает серверу статус и заголовки. Возвращает тело в байтах.
        
        Превращает тело в байты, вызывает start_response со статусом и заголовками.
        """

        body_bytes = self.body.encode("utf-8")

        headers = [
            ("Content-Type", self.content_type),
            ("Content-Length", str(len(body_bytes))),
        ]

        start_response(self.status, headers)

        return [body_bytes]