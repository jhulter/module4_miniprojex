import book_ops
import user_ops
import genre_ops
import author_ops
def main_menu():
    while True:
        try:
            print("Welcome to the Library Management System!")
            print("\n Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Enter a menu choice: ")
            if choice == "1":
                book_ops.books_menu()
            elif choice == "2":
                user_ops.user_menu()
            elif choice == "3":
                author_ops.author_menu()
            elif choice == "4":
                genre_ops.genre_menu()
            elif choice == "5":
                break
        except:
            print("An error has occured")

main_menu()
