from database_practise import library_system

def authenticate(username, password):
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
        print("Credentials are valid.")
        print(result)
    else:
        print("Invalid username or password.")

authenticate('arsh', '1234')