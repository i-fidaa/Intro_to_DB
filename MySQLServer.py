# MySQLServer.py

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (replace with your working username/password)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",        # <-- your MySQL username
            password="password" # <-- your MySQL password
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
