from html import escape


def get_value(env, name):
    """Получает переменную или поле записи из контекста."""
    parts = name.split(".")

    value = env[parts[0]]

    for part in parts[1:]:
        value = value[part]

    return value


class Text:
    """Обычный текст шаблона, включая HTML."""

    def __init__(self, text):
        self.text = text

    def render(self, env):
        return self.text


class Var:
    """Подстановка переменной."""

    def __init__(self, name):
        self.name = name

    def render(self, env):
        value = get_value(env, self.name)

        if value is None:
            return ""
        
        #Проверяем, является ли значение объектом класса Html.
        #Если является - возвращаем разметку не экранируя.
        if isinstance(value, Html):
            return value.text

        return escape(str(value))


class For:
    """Цикл с вложенными узлами."""

    def __init__(self, variable, collection, children):
        self.variable = variable
        self.collection = collection
        self.children = children

    def render(self, env):
        items = get_value(env, self.collection)

        result = ""

        for item in items:
            local_env = env.copy()
            local_env[self.variable] = item

            for child in self.children:
                result += child.render(local_env)

        return result


class Template:
    """Разбирает шаблон в дерево и получает готовый HTML."""

    def __init__(self, source):
        self.source = source
        self.position = 0
        self.children = self.parse()

    def parse(self, inside_for=False):
        """Читает узлы до конца шаблона или до endfor."""
        children = []

        while self.position < len(self.source):
            start = self.source.find("{{", self.position)

            # Если маркеров больше нет, остаток — обычный текст.
            if start == -1:
                text = self.source[self.position:]
                children.append(Text(text))

                self.position = len(self.source)
                break

            # Текст перед маркером сохраняем отдельным узлом.
            if start > self.position:
                text = self.source[self.position:start]
                children.append(Text(text))

            end = self.source.find("}}", start + 2)

            if end == -1:
                raise ValueError("Не найдена закрывающая скобка }}")

            command = self.source[start + 2:end].strip()

            # Следующее чтение начнётся после текущего маркера.
            self.position = end + 2

            if command == "":
                raise ValueError("Пустой маркер шаблона")

            parts = command.split()

            if parts[0] == "for":
                # Ожидаем: for p in products
                if len(parts) != 4:
                    raise ValueError(
                        "Цикл должен иметь вид: for p in products"
                    )

                if parts[2] != "in":
                    raise ValueError("В цикле пропущено слово in")

                variable = parts[1]
                collection = parts[3]

                if not variable.isidentifier():
                    raise ValueError("Неверное имя переменной цикла")

                # Читаем содержимое цикла до его endfor.
                body = self.parse(inside_for=True)

                node = For(variable, collection, body)
                children.append(node)

            elif parts[0] == "endfor":
                if len(parts) != 1:
                    raise ValueError("После endfor не должно быть текста")

                if not inside_for:
                    raise ValueError("endfor указан без начала цикла")

                return children

            else:
                # Обычная переменная: name или p.name.
                name_parts = command.split(".")

                for part in name_parts:
                    if not part.isidentifier():
                        raise ValueError(
                            "Неверное имя переменной: " + command
                        )

                children.append(Var(command))

        if inside_for:
            raise ValueError("Для цикла не найден endfor")

        return children

    def render(self, env=None):
        """Объединяет результаты всех узлов."""
        if env is None:
            env = {}

        result = ""

        for child in self.children:
            result += child.render(env)

        return result
    
class Html:
    """Готовая HTML-разметка, которую не нужно экранировать"""
    
    def __init__(self, text):
        self.text = text