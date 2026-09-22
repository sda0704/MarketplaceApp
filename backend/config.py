#region Сеть.

# Адрес сервера.
HOST = '127.0.0.1'

# Порт сервера.
PORT = 8000

#endregion

#region HTTP.

# Настройки разметки и кодировки HTTP запроса.
DEFAULT_CONTENT_TYPE = 'text/html; charset=utf-8'

# HTTP заголовок запроса.
CONTENT_TYPE_HEADER = 'Content-Type'

# Размер тела HTTP-запроса.
CONTENT_LENGTH_HEADER = 'Content-Length'

#endregion

#region Статусы HTTP.

# Ответ: OK
HTTP_OK = '200 OK'

# Ответ: NOT_FOUND
HTTP_NOT_FOUND = '404 Not Found'

# Ответ: Ошибка сервера.
HTTP_INTERNAL_ERROR = '500 Internal Server Error'

#endregion