import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yashika2004",
        database="hostel_db"
    )
