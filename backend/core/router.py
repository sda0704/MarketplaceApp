# Маршрутизатор.
class Router:
    #Создает пустой роутер.
    def __init__(self):
        self.routes = []

    # Добавляет маршрут вручную, без использования декоратора.
    def add(self, method, pattern, handler):
        self.routes.append((method.upper(), parse_pattern(pattern), handler))

    # Возвращает декоратор, который регистрирует функцию как
    # обработчик маршрута.
    def route(self, method, pattern):
        def decorator(handler):
            self.add(method, pattern, handler)
            return handler
        return decorator

    # Ищет обработчик по методу и пути, возвращая извлеченные 
    # параметры.
    def match(self, method, path):
        path_parts = parse_pattern(path)
        for route_method, pattern_parts, handler in self.routes:
            if route_method != method.upper():
                continue
            params = match_route(pattern_parts, path_parts)
            if params is not None:
                return handler, params
        return None, None

# Разбирает шаблон или путь на список непустых сегментов.
def parse_pattern(pattern):
    return [p for p in pattern.strip('/').split('/') if p]

def match_route(pattern_parts, path_parts):
    if len(pattern_parts) != len(path_parts):
        return None

    params = {}
    for pattern_part, path_part in zip(pattern_parts, path_parts):
        if is_param(pattern_part):
            name = extract_param_name(pattern_part)
            params[name] = path_part
        elif pattern_part != path_part:
            return None
    return params

# Проверяет, является ли сегмент шаблона параметром.
def is_param(part):
    return part.startswith('<') and part.endswith('>')

# Извлекает имя параметра из сегмента шаблона.
def extract_param_name(part):
    return part[1:-1]