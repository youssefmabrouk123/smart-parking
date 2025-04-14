import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Update with your actual MySQL password
    MYSQL_DB = 'smart_parking'
    MYSQL_CURSORCLASS = 'DictCursor'