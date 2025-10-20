import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # Initialize to avoid UnboundLocalError

    try:
        # Connect to MySQL server (update your password)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # ← Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully or already exists.")

    except Error as e:
        print(f"MySQL Error: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
