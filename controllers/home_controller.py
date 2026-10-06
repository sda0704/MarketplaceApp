from base_controller import BaseController
from decorators import route

class HomeController(BaseController):
    """Отвечает за главную страницу и страницу about"""

    @route("/", method="GET")
    def index(self):
        """Главная страница магазина."""
        html_page = """
        <h1>Добро пожаловать! </h1>
        <ul> 
            <li>
                <a href="/about">О нас</a>
            </li>
        </ul>
        """

        return self.html(html_page)

    @route("/about", method="GET")
    def about(self):
        html_page = """
        <h1>О нас </h1>
        <a href="/">На главную</a>
        """

        return self.html(html_page)