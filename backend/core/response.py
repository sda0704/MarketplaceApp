# Импортирует настройки из config.
from config import (
    HTTP_OK,
    DEFAULT_CONTENT_TYPE,
    CONTENT_LENGTH_HEADER,
    CONTENT_TYPE_HEADER
)

# Ответ.
class Response:
    #Создает объект ответа с телом, статусом и типом содержимого.
    def __init__(self, body='', status=HTTP_OK, content_type=DEFAULT_CONTENT_TYPE):
        if isinstance(body, str):
            body = body.encode('utf-8')
        self.body = body
        self.status = status
        self.content_type = content_type

    # Вызывает start_response и возвращает тело. 
    def __call__(self, start_response):
        headers = [
            (CONTENT_TYPE_HEADER, self.content_type),
            (CONTENT_LENGTH_HEADER, str(len(self.body))),
        ]
        start_response(self.status, headers)
        return [self.body]