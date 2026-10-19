import json
from html import escape
from pathlib import Path

from response import Response

from constants import _200, _404

class BaseController:
    """Базовый контроллер."""

    templates_dir = Path("templates")

    def __init__(self, request): 
        """Сохраняет объект запроса, чтобы наследники могли его использовать.
        
        request - объект класса Request с данными текущего запроса.
        """

        self.request = request

    def render(self, template_name, context=None):
        """Читает шаблон и подставляет значения.
        
        template_name - имя файла.
        context - Словарь {"метка": "значение"}
        """

        if context == None:
            context = {}

        template_path = self.templates_dir / template_name

        with open(template_path, "r", encoding="utf-8") as f:
            html = f.read()

        for key, value in context.items():
            # Экранируем значение, чтобы <, >, &, кавычки не сломали HTML.
            safe_value = escape(str(value))

            marker = "{{ " + key + " }}"

            html = html.replace(marker, safe_value)

        return html

    def build_page(self, title, content):
         """Оборачивает содержимое в общий каркас (base.html).

        title - заголовок окна.
        content - готовый HTML.
        """
         base_path = self.templates_dir / "base.html"

         with open(base_path, "r", encoding="utf-8") as f:
                html = f.read()

         html = html.replace("{{ title }}", escape(str(title)))
         html = html.replace("{{ content }}", content)

         return html

    def html(self, body, status = _200):
        """Возврашает html-ответ
        
        body - html строка.
        status - статус ответа. По умолчанию 200.
        """
        headers = [("Content-Type", "text/html; charset=utf-8")]

        return Response(body=body, status=status, headers=headers)

    def json(self, data, status = _200):
        """Возвращает json-ответ
        
        data - любой объект, который будет превращен в json.

        status - статус ответа. По умолчанию 200.
        """

        body = json.dumps(data, ensure_ascii=False)
        headers = [("Content-Type", "application/json; charset=utf-8")]

        return Response(body = body, status = status, headers=headers)

