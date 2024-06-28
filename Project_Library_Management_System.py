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
# - X Adding a new user with user details.
# - X Viewing user details.
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
from author import Author

def main():
    library = {} #this would be fine as a list too
    user_store = {}
    authors = {}
    while True:
        print("\nWelcome to the Library Management System!\n")
        try:
            main_menu_choice = int(input("Main Menu:\n1. Book Operations \n2. User Operations \n3. Author Operations\n4. Quit\n"))
            if main_menu_choice == 1:
                book_main(library, user_store, authors)
            elif main_menu_choice == 2:
                user_main(user_store)
            elif main_menu_choice == 3:
                author_main(authors)
            elif main_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-4\n")

def add_book(library, authors):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    genre = input("Enter the book's genre: ")
    try:
        pub_date = int(input("Enter the the book's publication date: Use the year: "))
    except ValueError:
        print("Thats not a number please give the 4 digit year XXXX: ")
    
    book = Book(title, author, genre, pub_date)
    library[title] = book #title is the key the value is the book object
    if author in authors:
        new_list = [title, genre, pub_date]
        authors[author].append([new_list])
    else:
        author = Author(author, [title, genre, pub_date])
        authors[author] = author



def search_book(library):
    title = input("What is the title you're looking for? ")
    if title in library:
        book = library[title]
        print("Book found, here is some info: ")
        print(book.title)
        print(book.author)
        print(book.genre)
        print(book.pub_date)
        print(book.get_availability())
    else:
        print("Sorry! That book is not in our library.")

def display_books(library):
    for book in library.values():
        print(f"{book.title} by {book.author}: Genre: {book.genre}: Published: {book.pub_date} Availibility: {book.get_availability()}")

def check_out(library, user_store):
    title = input("Please enter the book you'd like to check out: ")
    user_id = int(input("Please enter the library ID: "))  # Convert user_id to int
    if user_id in user_store:
        user = user_store[user_id]  # Retrieve user object
        if title in library:
            if library[title].borrow_book():
                user.assign_book(library[title])
                print(f"Book '{library[title].title}' has been checked out to {user.name}.")
            else:
                print("Book is not available.")
        else:
            print("Book not found.")
    else:
        print("User not found.")

def return_book (library, user_store):
    user_id = int(input("Please enter the library ID: "))
    title = input("Please enter the book you'd like to return: ")
    if user_id in user_store:
        user = user_store[user_id]
        book = library[title]
        if book and book in user.borrowed_books:
            user.remove_book(book)
            book.return_book()
            print(f"Book '{book.title}' has been returned by {user.name}.")
        else:
            print("Book not found in user's borrowed list.")
    else:
        print("User not found.")

def book_main(library, user_store, authors):
    while True:
        try:
            book_menu_choice = int(input("\nBook Operations: \n1. Add a new book \n2. Checkout a book \n3. Return a book \n4. Search for a book \n5. Display all books \n6. Return to Main Menu \n"))
            if book_menu_choice == 1:
                add_book(library, authors)
                pass
            elif book_menu_choice == 2:
                check_out(library, user_store)
                pass
            elif book_menu_choice == 3:
                return_book(library, user_store)
                pass
            elif book_menu_choice == 4:
                search_book(library)
                pass
            elif book_menu_choice == 5:
                display_books(library)
                pass
            elif book_menu_choice == 6:
                break
            else:
                print("\nPlease choose a number between 1-6\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-6\n")


def add_user(user_store):
    print("Add User Tab")
    name = input("Name: ")
    email = input("Email: ")
    # user_id = name.generate_user_id()
    user = User(name, email)
    user.generate_user_id()
    user_id = user.get_user_id()
    user_store[user_id] = user #title is the key the value is the book object
    print(f"{user.get_user_id()} ID has been assigned to the new user {user.name}. Keep it secret, keep it safe!")
    print(user_store)

def search_user(user_store):
    user_id = int(input("Please input the user ID that was assigned"))
    if user_id in user_store:
        user = user_store[user_id]
        print("User Found, here is some info: ")
        print(user.get_user_id())
        print(user.name)
        print(user.get_user_email())
        user.get_borrowed_books()
    else:
        print("Looks like that an incorect User")

def display_users(user_store):
    for user in user_store.values():
        print(f"User ID: {user.get_user_id()} \nUsername: {user.name} \nEmail: {user.get_user_email()} \nBooks checked out:")
        user.get_borrowed_books()

def user_main(user_store):
    while True:
        try:
            book_menu_choice = int(input("\nUser Operations: \n1. Add a new user \n2. View user details \n3. Display all users \n4. Return to Main Menu \n"))
            if book_menu_choice == 1:
                add_user(user_store)
            elif book_menu_choice == 2:
                search_user(user_store)
            elif book_menu_choice == 3:
                display_users(user_store)
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