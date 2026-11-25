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

        env = {
            "products": products
        }   
        
        content = self.render("products.html", env)
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