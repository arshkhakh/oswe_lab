from login import authenticate
from backend.app.register import register
from backend.app.books import add_book,search_book

def main_menu():
    while True:
        print("1. Login")
        print("2. register")
        print("3. add book")
        print("4. search book")
        print("5. exit")

        console = input("Enter the option: ")
        print(f"You selected {console}")

        if console == str(1):
            user = input("Enter Username: ")
            passwd = input("Enter Password: ")
            authenticate(user,passwd)
            break

        if console == str(2):
            new_user = input("Enter new username")
            new_passwd = input("Enter a password")
            register(new_user,new_passwd)
            break

        if console == str(3):
            title = input("Enter book title")
            author = input("Enter author name")
            add_book(title,author)
            break

        if console == str(4):
            book_title = input("Enter Book title: ")
            search_book(book_title)
            break

main_menu()