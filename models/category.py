from database import get_connection

def get_all():
    """Получает все категории."""
    connection = get_connection()
    
    try:
        return connection.execute(
             """
            SELECT id, name, description
            FROM categories
            ORDER BY id
            """
        ).fetchall()
    finally:
        connection.close()


def get_by_id(category_id):
    """Получает категорию по идентификатору."""
    connection = get_connection()
    
    try:
        return connection.execute(
              """
            SELECT id, name, description
            FROM categories
            WHERE id = ?
            """,
            (category_id,),
        ).fetchone()
    finally:
        connection.close()