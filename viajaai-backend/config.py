import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development') 

    # Banco de dados
    DB_HOST = os.environ.get('DB_HOST', 'mysql')
    DB_USER = os.environ.get('DB_USER', 'myuser')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'mypassword')
    DB_NAME = os.environ.get('DB_NAME', 'mydatabase')
    DB_PORT = os.environ.get('DB_PORT', '3306')