from database import library_system

current_user = None

def authenticate(username, password):
    global current_user
    conn = library_system()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()

    if result:
        current_user = username
        print("Credentials are valid.")
        return True  # Return True if credentials are valid
    else:
        print("Invalid username or password.")
        return False  # Return False if credentials are invalid