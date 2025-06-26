# database/setup.py
import psycopg2
from psycopg2.extras import RealDictCursor
import config as config
from database.schema import Define_Tables_Schema
from utils.prints import success, error, info

connection = None
cursor = None
def Get_Connection():
    global connection, cursor
    if connection is None or cursor is None:
        Setup_Database()
    return connection, cursor 


def Setup_Database():
    global connection, cursor

    try:
        connection = psycopg2.connect(
            host=config.DB_HOST,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            port=config.DB_PORT,
            cursor_factory=RealDictCursor
        )
        cursor = connection.cursor()

        cursor.execute('SELECT VERSION()')
        version = cursor.fetchone()

        success("Database connection established successfully.")
        info(f"🗄️  Database version: {version}")

        # Define the database schema
        Define_Tables_Schema()

    except psycopg2.Error as e:
        error(f"\n❌ Database connection failed: {e}\n")

