from user import AdminUser
from user import RegularUser
from book import Book


class Library:
    # TODO
    def main(self, user_type):
        if user_type == 1:
            print("""
            1. Create a new user
            2. Create a new book
            3. Borrow a book
            4. Return a book
            5. List all books
            6. List all users
            7. List all borrowed books
            8. Exit
            """)
        elif user_type == 0:
            print("""
            1. Borrow a book
            2. Return a book
            3. Exit
            """)
        try:
            selection = int(input("Select an option: "))
            return selection
        except ValueError:
            return 0

    def create_user(self, username, password, user_type):
        i = 0
        with open("users.txt", "r") as file:
            users = []
            for user in file.readlines():
                users.append(user.strip("\n").split(":"))
        for user in users:
            if user[1] == username:
                i = 1
            else:
                continue
        if i == 0:
            if user_type == 1:
                AdminUser(username, password)
            elif user_type == 2:
                RegularUser(username, password)
        else:
            print("User already exists")

    def create_book(self, title, author, pb_year, n_copies):
        Book(title, author, pb_year, n_copies)

    def borrow_book(self):
        Book.borrow_book(self)

    def return_book(self, book):
        pass

    def list_books(self):
        with open("books.txt", "r") as file:
            books = []
            for book in file.readlines():
                books.append(book.strip("\n").split(":"))
        for book in books:
            print(
                f"Book Title: {book[1]}\nBook Author: {book[2]}\nPublication Year: {book[3]}\nNumber of copies available: {book[4]}\n"
            )

    def list_users(self):
        with open("users.txt", "r") as file:
            for line in file.readlines():
                print(line.strip("\n"))

    def list_borrowed_books(self):
        pass


def get_users(username, password):
    with open("users.txt", "r") as file:
        users = []
        for user in file.readlines():
            users.append(user.strip("\n").split(":"))
    for user in users:
        if user[1] == username:
            if user[2] == password:
                if user[3] == "1":
                    return 1
                elif user[3] == "0":
                    return 0
            else:
                print("Wrong password")
                return
        else:
            continue
    return print("User not found")


if __name__ == "__main__":
    library = Library()
    print("Welcome to the library!")
    while True:
        try:
            print("1: Login")
            print("2: Exit")
            option = int(input("Select an option: "))
            if option == 1:
                usr_login = str(input("Username: "))
                usr_pass = str(input("Password: "))
                user_exists = get_users(usr_login, usr_pass)
                if user_exists == 1:
                    x = library.main(user_exists)
                    while x != 8:
                        if x == 1:
                            user_type = int(
                                input(
                                    "1: Admin user\n2: Regular user\nSelect an option: "
                                ))
                            if user_type == 1 or user_type == 2:
                                username = str(input("Username: "))
                                password = str(input("Password: "))
                                library.create_user(username, password,
                                                    user_type)
                            else:
                                print("Invalid input")
                            x = library.main(user_exists)
                        elif x == 2:
                            b_title = str(input("Enter book title: "))
                            b_author = str(input("Enter author name: "))
                            pb_year = int(input("Enter year of publication: "))
                            n_copies = int(input("Enter number of copies: "))
                            library.create_book(b_title, b_author, pb_year,
                                                n_copies)
                            x = library.main(user_exists)
                        elif x == 3:
                            library.borrow_book()
                            x = library.main(user_exists)
                        elif x == 4:
                            library.return_book()
                            x = library.main(user_exists)
                        elif x == 5:
                            library.list_books()
                            x = library.main(user_exists)
                        elif x == 6:
                            library.list_users()
                            x = library.main(user_exists)
                        elif x == 7:
                            library.list_borrowed_books()
                            x = library.main(user_exists)
                        elif x == 8:
                            print("Exiting...")
                        else:
                            print("Invalid option")
                            x = library.main(user_exists)
                elif user_exists == 0:
                    x = library.main(user_exists)
                    while x != 3:
                        if x == 1:
                            library.borrow_book()
                            x = library.main(user_exists)
                        elif x == 2:
                            library.return_book()
                            x = library.main(user_exists)
                        elif x == 3:
                            print("Exiting...")
                        else:
                            print("Invalid option")
                            x = library.main(user_exists)
            elif option == 2:
                print("Exiting...")
                print("Have a nice day!")
                break
            else:
                print("Invalid option")
        except ValueError as e:
            print("Invalid input")
