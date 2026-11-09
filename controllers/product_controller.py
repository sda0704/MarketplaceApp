"""Контроллер товаров."""
from base_controller import BaseController
from decorators import route
from models import product as product_model


class ProductController(BaseController):
    """Отвечает за страницы товаров."""

    @route("/products", method="GET")
    def list(self):
        """Страница со списком всех товаров."""
        products = product_model.get_all()

        cards = ""
        for p in products:
            name = p["name"]
            description = p["description"]
            price = p["price"]

            cards += f"""
                <div class="card">
                    <h3>{name}</h3>
                    <p>{description}</p>
                    <p><b>{price} ₽</b></p>
                </div>
            """

        content = f"""
            <h1>Каталог товаров</h1>
            <div class="products">{cards}</div>
        """

        page = self.build_page("Каталог", content)
        return self.html(page)