import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
import os

class DatabaseManager:
    # COnfiguracao do banco de dados
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST', 'mysql'),
            'user': os.getenv('DB_USER', 'myuser'),
            'password': os.getenv('DB_PASSWORD', 'mypassword'),
            'database': os.getenv('DB_NAME', 'mydatabase'),
            'port': os.getenv('DB_PORT', '3306'),
            'autocommit': False
        }

    @contextmanager
    def get_connection(self):
        # Metodo que retorna a conexão do banco de dados
        conn = None
        try:
            conn = mysql.connector.connect(**self.config)
            yield conn
            conn.commit()
        except Error as e:
            if conn:
                conn.rollback()
            raise Exception(f"Database error: {str(e)}")
        finally:
            if conn and conn.is_connected():
                conn.close()
