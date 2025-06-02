from database import library_system

#Global variable -> define the variable outside of any function will simply make it global varialble
# created for authentication purpose, 
current_user = None

def authenticate(username, password):
    global current_user
    conn = library_system()
    cursor = conn.cursor() #cursor is used to execute SQL queries against the database ex: SELECT, INSERT etc

    #cursor supports parameterized queries, which help prevent SQL injection
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password)) 

    #fetchone return the next row of a query result
    result = cursor.fetchone()

    #always close connection to avoid performance issues, data integrity
    cursor.close()
    conn.close()

    # Check if a result was found
    if result:
        current_user = username
        print("Credentials are valid1.")
        print(result)
        return True
    else:
        print("Invalid username or password.")
        return False

#authenticate('arsh', '1234')