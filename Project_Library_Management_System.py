    # Welcome to the Library Management System!

    # Main Menu:
    # 1. Book Operations
    # 2. User Operations
    # 3. Author Operations
    # 4. Quit


# - X Adding a new book with all relevant details.
# - X (book) Allowing users to borrow a book, marking it as "Borrowed." 
# - X (book) Allowing users to return a book, marking it as "Available."
# - X Searching for a book by its unique identifier (title) and displaying its details.
# - X Displaying a list of all books with their unique identifiers.
# - Adding a new user with user details.
# - Viewing user details.
# - Displaying a list of all users.
# - Adding a new author with author details.
# - Viewing author details.
# - Displaying a list of all authors.
# - Adding a new genre with genre details.
# - Viewing genre details.
# - Displaying a list of all genres.
# - Quitting the application.

from book import Book
from user import User


def main():
    while True:
        print("\nWelcome to the Library Management System!\n")
        try:
            main_menu_choice = int(input("Main Menu:\n1. Book Operations \n2. User Operations \n3. Author Operations\n4. Quit\n"))
            if main_menu_choice == 1:
                book_main()
            elif main_menu_choice == 2:
                user_main()
            elif main_menu_choice == 3:
                author_main()
            elif main_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-4\n")

def add_book(library):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    genre = input("Enter the book's genre: ")
    try:
        pub_date = int(input("Enter the the book's publication date: Use the year: "))
    except ValueError:
        print("Thats not a number please give the 4 digit year XXXX: ")
    book = Book(title, author, genre, pub_date)
    library[title] = book #title is the key the value is the book object

def search_book(library):
    title = input("What is the title you're looking for? ")
    if title in library:
        book = library[title]
        print("Book found, here is some info: ")
        print(book.title())
        print(book.author())
        print(book.genre())
        print(book.pub_date())
        print(book.get_availability())
    else:
        print("Sorry! That book is not in our library.")

def display_books(library):
    for book in library.values():
        print(f"{book.title()} by {book.author()}: {book.genre()}: {book.get_availability()}")

def check_out(library, current_loans):
    title = input("Please enter the book you'd like to check out")
    # user will eventually come from another class - this could be a username or user id from a user object
    user = input("Please enter the library id")
    # checks if the title(key) is in the library and checking if we can borrow the book
    if title in library and library[title].borrow_book():
        current_loans[title] = user
        #               using the getter for the title
        print(f"Book {library[title].title()} has been checked out to {user}")
    else:
        print("Book is not available or not found")

def book_main():
    library = {} #this would be fine as a list too
    current_loans = {}
    while True:
        try:
            book_menu_choice = int(input("\nBook Operations: \n1. Add a new book \n2. Borrow a book \n3. Return a book \n4. Search for a book \n5. Display all books \n6. Return to Main Menu \n"))
            if book_menu_choice == 1:
                add_book(library)
                pass
            elif book_menu_choice == 2:
                pass
            elif book_menu_choice == 3:
                pass
            elif book_menu_choice == 4:
                search_book(library)
                pass
            elif book_menu_choice == 5:
                pass
            elif book_menu_choice == 6:
                break
            else:
                print("\nPlease choose a number between 1-6\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-6\n")

def add_user():
    print("Add User Tab")
    name = input("Name: ")
    email = input("Email: ")
    user_id = name.generate_user_id()
    user = User(name, email, user_id)




    pass

def user_main():
    while True:
        try:
            book_menu_choice = int(input("\nUser Operations: \n1. Add a new user \n2. View user details \n3. Display all users \n4. Return to Main Menu \n"))
            if book_menu_choice == 1:
                pass
            elif book_menu_choice == 2:
                pass
            elif book_menu_choice == 3:
                pass
            elif book_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-4\n")

def author_main():
    while True:
        try:
            book_menu_choice = int(input("\nAuthor Operations: \n1. Add a new author \n2. View author details \n3. Display all authors \n4. Return to Main Menu \n"))
            if book_menu_choice == 1:
                pass
            elif book_menu_choice == 2:
                pass
            elif book_menu_choice == 3:
                pass
            elif book_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-4\n")
main()