from database import get_connection;

def get_all():
    """Получает все товары"""
    connection = get_connection()
    
    try:
        return connection.execute(
            """
            SELECT id, name, description, price, category_id
            FROM products
            ORDER BY id
            """
        ).fetchall()
    finally:
        connection.close()
        

def get_by_id(product_id):
    """Получает товар по Id. Возвращает None, если товар не найден"""
    connection = get_connection()
    
    try:
        return connection.execute(
               """
            SELECT id, name, description, price, category_id
            FROM products
            WHERE id = ?
            """,
            (product_id,),
        ).fetchone()
    finally:
        connection.close()
        
def get_by_category(category_id):
    """Получает товары выбранной категории"""
    connection = get_connection()
    
    try:
        return connection.execute(
            """
            SELECT id, name, description, price, category_id
            FROM products
            WHERE category_id = ?
            ORDER BY id
            """,
            (category_id,),
        ).fetchall()
    finally:
        connection.close()