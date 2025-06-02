def main_menu():
    while True:
        print("1. Login")
        print("2. register")
        print("3. search book")
        print("4. exit")

        console = input("Enter the option: ")
        print(f"You selected {console}")

        if console == str(1):
            print("Option 1 selected")
    

main_menu()