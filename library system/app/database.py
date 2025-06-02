import mysql.connector
from mysql.connector import Error

def library_system():
    conn = None
    try:
        conn = mysql.connector.connect(
            user = 'root',
            host = 'localhost',
            database = 'library_system',
            passwd = '1234'
        )
        if conn.is_connected():
            print("Database connection sucessfull")
            return conn #return connection object otherwise will be 'None' by default
    except Error as e:
        print("Error:",e)
    return conn
library_system()