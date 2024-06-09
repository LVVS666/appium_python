from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

class DbConnect:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv('host'),
            port=os.getenv('port'),
            database=os.getenv('database'),
            user=os.getenv('user'),
            password=os.getenv('password'),
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def search_zone(self, phone):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT zone FROM users WHERE phone = %s AND deleted_at IS NULL;",
                    (phone,)
                )
                result = cursor.fetchone()
                return result[0] if result else None
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return None



