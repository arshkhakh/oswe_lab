from database import library_system
from mysql.connector import Error
from login import current_user #used for authentication

def check_authentication():
    if current_user == None:
        print("you must be logged in to perform this action")
        #print(current_user) -> used to check what's inside current user
        return False #the function immediately exits
    return True

#add a book
def add_book(title, author):
    conn = library_system()
    cursor = conn.cursor()

    try:
        query = "INSERT INTO books (title, author) VALUES ('" + title + "', '" + author + "')"
        cursor.execute(query)
        conn.commit()
        print("book added successfull")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

#search a book
def search_book(title):
    conn = library_system()
    cursor = conn.cursor()

    query = f"SELECT * FROM books WHERE TITLE = '{title}'"
    cursor.execute(query)

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        print(f"Book: '{title}' found")
    else:
        print("Book not available")

#remove a book
def remove_book(title):
    conn = library_system()
    cursor = conn.cursor()

    query = f"DELETE * FROM books WHERE TITLE = '{title}'"
    cursor.execute(query)

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        print(f"Book: '{title}' has been removed")
    else:
        print("Book not available to remove.")

check_authentication()
# add_book('Pro Git','Scott Chacon')