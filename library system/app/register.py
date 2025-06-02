from backend.app.database import library_system
from mysql.connector import Error

def register(username, password):
    conn = library_system()
    cursor = conn.cursor() #cursor is used to execute SQL queries against the database ex: SELECT, INSERT etc

    try:
        #parameterized queries, which help prevent SQL injection 
        #parameterized queries, the SQL command is defined with placeholders (often represented with symbols such as %s, ?, etc.) while actual data is passed separately.
        """"
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        """

        query = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')"
        cursor.execute(query)


        #changes made in a transaction are successfully applied to the database like INSERT, UPDATE
        conn.commit()    
        print("Registration successful!")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()


# register('prab', '131313')