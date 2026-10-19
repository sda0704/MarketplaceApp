from base_controller import BaseController
from decorators import route

class HomeController(BaseController):
    """Отвечает за главную страницу и страницу about"""

    @route("/", method="GET")
    def index(self):
        """Главная страница магазина."""

        content = self.render("home.html")

        page = self.build_page("Главная", content)

        return self.html(page)

    @route("/about", method="GET")
    def about(self):
        content = self.render("about.html")

        page = self.build_page("О нас", content)

        return self.html(page)