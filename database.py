import sqlite3
from pathlib import Path

DB_PATH = Path("shop.db")

def get_connection():
    """Открывает соединение с базой данных."""

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    return connection

def init_db():
    """Создает таблицы категории и продукты."""

    connection = get_connection()

    connection.executescript("""
        CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
        );

        CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        );
    """)

    connection.commit()
    connection.close()



def seed_db():
    """Заполняет БД тестовыми записями."""

    connection = get_connection()

    #Считаем количество записей. Если их больше 0, значит записи уже созданы.
    count = connection.execute("SELECT COUNT(*) FROM products").fetchone()[0]

    if count > 0:
        connection.close()

        return

    connection.executescript("""
        INSERT INTO categories (name, description) VALUES
        ('Электроника', 'Телефоны, ноутбуки, планшеты'),
        ('Книги', 'Художественная и учебная литература'),
        ('Одежда', 'Футболки, куртки, обувь');
     """)


    connection.executescript("""
        INSERT INTO products (name, description, price, category_id) VALUES
            ('Смартфон','Хороший телефон',30000, 1),
            ('Ноутбук','Мощный ноутбук',80000, 1),
            ('Наушники','Беспроводные',5000, 1),
            ('Роман "Война и мир"', 'Толстой, 4 тома',      1500, 2),
            ('Учебник Python','Для начинающих',2000, 2),
            ('Футболка','Хлопок, белая',1200, 3),
            ('Джинсы','Синие, классические',3500, 3),
            ('Куртка', 'Зимняя, тёплая',7000, 3);
    """)

    connection.commit()
    connection.close()



if __name__ == "__main__":
    """При запуске этого файла создаем таблицы и заполняем."""
    
    init_db()
    seed_db()