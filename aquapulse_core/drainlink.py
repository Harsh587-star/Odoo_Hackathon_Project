import mysql.connector
from puddle_config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
