"""Контроллер товаров."""
from base_controller import BaseController
from decorators import route
from models import product as product_model
from constants import _404


class ProductController(BaseController):
    """Отвечает за страницы товаров."""

    @route("/products", method="GET")
    def list(self):
        """Страница со списком всех товаров."""
        products = product_model.get_all()

        cards = ""
        for p in products:
            product_id = p["id"]
            name = p["name"]
            description = p["description"]
            price = p["price"]

            cards += f"""
                <div class="card">
                    <h3>
                        <a href="/product/{product_id}">{name}</a>
                    </h3>
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
    
    def detail(self, product_id):
        """Показывает страницу одного товара"""
        product = product_model.get_by_id(product_id)
        
        if product is None:
            return self.html(
                "<h1>Товар не найден</h1>",
                status=_404
            )
            
        content = self.render(
             "product_detail.html",
            {
            "name": product["name"],
            "description": product["description"] or "",
            "price": product["price"]
            }
        )
        
        page = self.build_page(product["name"], content)
        
        return self.html(page)