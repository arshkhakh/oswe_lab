from backend.app.database import library_system

def authenticate(username,password):
    conn = library_system()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' and password = '{password}'"
    # query1 = "SELECT * FROM users"
    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        print("Credentials are valid.")
        # print(result)
    else:
        print("Invalid username or password.")

authenticate('arsh', '1234')