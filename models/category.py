from database import get_connection

def get_all():
    """Получает все категории."""
    
    connection = get_connection()
    
    rows = connection.execute("SELECT id, name, description FROM categories").fetchall()
    
    connection.close()
    return rows


def get_by_id(category_id):
    """Получает категорию по идентификатору."""
    connection = get_connection()
    
    row = connection.execute(
        "SELECT id, name, desctiption FROM categories WHERE id = ?",
        (category_id)
    ).fetchone()
    
    connection.close()
    return row