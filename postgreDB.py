import psycopg2

class PostgreDB:
    def __init__(self, connection_string):
        """Конструктор объекта класса подключения к базе данных"""
        self.connection = psycopg2.connect(connection_string)
        self.cursor = self.connection.cursor()

    def get_user_position(self, user_id):
        """Загрузка позиции пользователя"""
        self.cursor.execute(f"""SELECT positionId FROM user_position WHERE id = {user_id}""")
        results = self.cursor.fetchone()
        if results:
            return results
        else:
            self.cursor.execute(f"""INSERT INTO user_position VALUES ({user_id}, 0)""")
            self.connection.commit()
            return 0

    def update_user_position(self, user_id, new_position):
        """Обновление позиции пользователя"""
        self.cursor.execute(f"""UPDATE positionId SET position = {new_position} WHERE id = {user_id}""")
        self.connection.commit()
        results = self.cursor.fetchone()
        if results:
            return results
        else:
            self.cursor.execute(f"""INSERT INTO user_position VALUES ({user_id}, 0)""")
            return 0 
        

    def create_users_table(self):
        """Создание таблицы с данными о пользователе"""
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS users
( ID INT PRIMARY KEY,
firtname VARCHAR(255),
lastname VARCHAR(255),
age INT,
gender INT CHECK (gender IN(1, 2)),
city VARCHAR(100),
relation INT CHECK (relation >= 0 and relation <8)
)"""
        )
        self.connection.commit()
    
    def create_user_position_table(self):
        """Создание таблицы с данными о позиции пользователя в меню"""
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS user_position
( ID INT PRIMARY KEY,
positionId INT
);"""
    )
        
    def create_user_pairs_table(self):
        """Создание таблицы с данными о подходящих парах"""
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS user_pairs(
ID INT,
pair_id INT
);"""
    )
        self.connection.commit()

    def __del__(self):
        self.connection.close()
        
