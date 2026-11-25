import json
from pathlib import Path
from template import Template, Html
from response import Response

from constants import _200

class BaseController:
    """Базовый контроллер."""

    templates_dir = Path("templates")

    def __init__(self, request): 
        """Сохраняет объект запроса, чтобы наследники могли его использовать.
        
        request - объект класса Request с данными текущего запроса.
        """

        self.request = request

    def render(self, template_name, env=None):
        """Читает шаблон и подставляет значения."""

        template_path = self.templates_dir / template_name
        
        with open(template_path, "r", encoding="utf-8") as f:
            source = f.read()
            
        template = Template(source)
            
        return template.render(env)

    def build_page(self, title, content):
        """Вставляет содержимое страницы в общий шаблон."""
         
        env = {
            "title": title,
            "content": Html(content)
        }

        return self.render("base.html", env)

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

