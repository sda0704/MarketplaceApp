from database import get_connection

def get_all():
    """Получает все продукты."""
    connection = get_connection()
    
    rows = connection.execute(
        "SELECT id, name, description, price, category_id FROM products"
    ).fetchall()
    
    connection.close()
    return rows

def get_by_id(product_id):
    """Получает продукт по идентификатору."""
    connection = get_connection()
    
    row = connection.execute(
        "SELECT id, name, description, price, category_id FROM products WHERE id = ?",
        (product_id)
    ).fetchone()
    
    connection.close()
    return row

def get_by_category(category_id):
    """Получает все продукты из категории."""
    connection = get_connection()
    
    rows = connection.execute(
       "SELECT id, name, description, price, category_id FROM products WHERE category_id = ?",
       (category_id)
    ).fetchall()
    
    connection.close()
    return rows