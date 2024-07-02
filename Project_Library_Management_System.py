from book import Book
from user import User
from author import Author
import re

def main(): # Main function to run the program
    library = {} 
    user_store = {}
    authors = {}
    while True:
        print("\nWelcome to the Library Management System!\n")
        try:
            main_menu_choice = int(input("Main Menu:\n1. Book Operations \n2. User Operations \n3. Author Operations\n4. Quit\n"))
            if main_menu_choice == 1:
                book_main(library, user_store, authors) # Calls the book_main function
            elif main_menu_choice == 2:
                user_main(user_store) # Calls the user_main function
            elif main_menu_choice == 3:
                author_main(authors, library) # Calls the author_main function
            elif main_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError: # If the user enters a letter instead of a number
            print("\nThats not a number! PLease choose a number between 1-4\n")

def add_book(library, authors):# Function to add a book to the library
    title = input("Enter the book's title: ").title()
    if title not in library: # If the book is not already in the library
        author_name = input("Enter the book's author: ").title()
        genre = input("Enter the book's genre: ").capitalize()
        try:
            pub_date = int(input("Enter the the book's publication date: Use the year: "))
        except ValueError:
            print("That's not a number, please give the 4-digit year XXXX: ")
            return

        book = Book(title, author_name, genre, pub_date) # Creates a new book object
        library[title] = book # title is the key, the value is the book object / Adds the book to the library

        if author_name in authors: # If the author is already in the authors dictionary
            new_list = [title, genre, pub_date] # Create a new list with the book's info
            authors[author_name].bio.append(new_list) # Append the new list to the author's bio
        else:
            author = Author(author_name, [[title, genre, pub_date]]) # Create a new author object
            authors[author_name] = author # author_name is the key, the value is the author object / adds the author to the authors dictionary
    else:
        print("Looks like that book is already in the library.")



def search_book(library, authors):
    title = input("What is the title you're looking for? ").title() # Get the title of the book the user is looking for
    if title in library: # If the book is in the library
        for book in library.values(): # Loop through the books in the library
            author = authors[book.author] # Get the author object from the authors dictionary
            print("Book found, here is some info: \n") 
            print(f"{book.title} by {author.name} \nGenre: {book.genre} \nPublished: {book.pub_date} \nAvailibility: {book.get_availability()}") # Print the book's info
    else:
        print("\nSorry! That book is not in our library.")

def display_books(library, authors):
    for book in library.values(): # Loop through the books in the library
        author = authors[book.author] # Get the author object from the authors dictionary
        print(f"{book.title} by {author.name} Genre: {book.genre} Published: {book.pub_date} Availibility: {book.get_availability()}") # Print the book's info

def check_out(library, user_store):
    title = input("Please enter the book you'd like to check out: ").title() # Get the title of the book the user wants to check out
    user_id = int(input("Please enter the library ID: "))  # Get the user's library ID
    if user_id in user_store:
        user = user_store[user_id]  # Get the user object from the user_store dictionary
        if title in library: # If the book is in the library
            if library[title].borrow_book(): # If the book is available
                user.assign_book(library[title]) # Assign the book to the user
                print(f"Book '{library[title].title}' has been checked out to {user.name}.") # print the book and who its checked out to
            else:
                print("Book is not available.")# If the book is not available
        else:
            print("Book not found.") # If the book is not in the library
    else:
        print("User not found.") # If the user is not in the user_store dictionary

def return_book (library, user_store):
    user_id = int(input("Please enter the library ID: ")) # Get the user's library ID
    title = input("Please enter the book you'd like to return: ").title() # Get the title of the book the user wants to return
    if user_id in user_store:
        user = user_store[user_id] # Get the user object from the user_store dictionary
        book = library[title] # Get the book object from the library dictionary
        if book and book in user.borrowed_books: # If the book is in the user's borrowed books
            user.remove_book(book) # call the remove_book method from the user class
            book.return_book() # Call the return_book method from the book class
            print(f"Book '{book.title}' has been returned by {user.name}.") # Print the book and who returned it
        else:
            print("Book not found in user's borrowed list.") # If the book is not in the user's borrowed books
    else:
            print("User not found.") # If the user is not in the user_store dictionary

def book_main(library, user_store, authors): # Function to run the book operations
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
                search_book(library, authors)
                pass
            elif book_menu_choice == 5:
                display_books(library, authors)
                pass
            elif book_menu_choice == 6:
                break
            else:
                print("\nPlease choose a number between 1-6\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-6\n")

def verify_email(email):
    pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}") # Define the regex pattern for email
    if re.match(pattern, email): # Check if the email matches the pattern
        return True
    else:
        return False

def add_user(user_store):
    print("Add User Tab")
    name = input("Name: ").title()# Get the user's name
    while True:
        email = input("Email: ").capitalize()
        if verify_email(email): #Verify the email is in the correct format
            break
        else:
            print("Invalid email, please use the syntax xxx@xxx.xxx")

    user = User(name, email) # Create a new user object
    user.generate_user_id() # call the generate_user_id method from the user class to generate a 4 digit library ID
    user_id = user.get_user_id() # Get the user's library ID
    user_store[user_id] = user # user_id is the key, the value is the user object / Add the user to the user_store dictionary
    print(f"\nLibrary ID #{user.get_user_id()} has been assigned to the new user {user.name}. Keep it secret, keep it safe!") # Print the user's library ID

def search_user(user_store): # Function to search for a user
    try:
        user_id = int(input("Please enter your 4 digit Library ID #: ")) # Get the user's library ID
        if user_id in user_store: # If the user is in the user_store dictionary
            user = user_store[user_id]  # Get the user object from the user_store dictionary
            print("User Found, here is some info: ")
            print(user.get_user_id())
            print(user.name)
            print(user.get_user_email())
            user.get_borrowed_books()
        else:
            print("Looks like that an incorect User")
    except ValueError:
        print("Thats not a number! Please Enter the 4 digit Library ID #: ")

def display_users(user_store): # Function to display all users
    for user in user_store.values(): # Loop through the users in the user_store dictionary
        print(f"Library ID# {user.get_user_id()} Name: {user.name} Email: {user.get_user_email()} Books checked out:") # Print the user's library ID, name, email, and borrowed books
        user.get_borrowed_books()
        

def user_main(user_store): # Function to run the user operations
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

def add_author(authors, library):
    author_name = input("Enter the author's name: ").title() # Get the author's name

    if author_name not in authors:
        print("Now let's add a book to the author's BIO") # If the author is not already in the authors dictionary
        title = input("Enter the book's title: ").title() # Get the book's title
        genre = input("Enter the book's genre: ").capitalize() # Get the book's genre
        try:
            pub_date = int(input("Enter the book's publication date: Use the year: "))
        except ValueError:
            print("That's not a number, please give the 4-digit year XXXX: ")
            return
        
        author = Author(author_name, [[title, genre, pub_date]]) # Create a new author object
        authors[author_name] = author

        if title not in library: # If the book is not already in the library
            book = Book(title, author_name, genre, pub_date)  # Create a new book object
            library[title] = book   # title is the key, the value is the book object / Adds the book to the library
        else: 
            print("Looks like that book is already associated with that author.")
    else:
        add_works = input("Looks like that author already exists. Would you like to add more works? Yes or No: ").lower() # If the author is already in the authors dictionary see if theyd like to add new book
        if add_works == "yes": 
            title = input("Enter the book's title: ").title()
            genre = input("Enter the book's genre: ").capitalize()
            try:
                pub_date = int(input("Enter the book's publication date: Use the year: "))
            except ValueError:
                print("That's not a number, please give the 4-digit year XXXX: ")
                return
            
            new_list = [title, genre, pub_date] # Create a new list with the book's info
            authors[author_name].bio.append(new_list)  # Append the new list to the author's bio
            
            if title not in library: # If the book is not already in the library
                book = Book(title, author_name, genre, pub_date)    # Create a new book object
                library[title] = book   # title is the key, the value is the book object / Adds the book to the library
            else:
                print("Looks like that book is already associated with that author.")
        else:
            print("No new works added for this author.")

def search_authors(authors):
    author_search = input("Which wuthor would you like to search for. ").title()
    if author_search in authors: # If the author is in the authors dictionary
            print(f"Author: {author_search}") # Print the author's name
            print("Books:")
            for book_info in authors[author_search].bio:    # Loop through the author's bio
                title, genre, pub_date = book_info  # Unpack the book info
                print(f" - Title: {title}, Genre: {genre}, Publication Date: {pub_date}")   # Print the book's info

def display_authors(authors):
    print("List of Authors:")
    for author_name, author in authors.items():
        print(f"Author: {author_name}")
        print("Books:")
        for book_info in author.bio:
            title, genre, pub_date = book_info
            print(f" - Title: {title}, Genre: {genre}, Publication Date: {pub_date}")
        print()
        

def author_main(authors, library): # Function to run the author operations
    while True:
        try:
            book_menu_choice = int(input("\nAuthor Operations: \n1. Add a new author \n2. View author details \n3. Display all authors \n4. Return to Main Menu \n"))
            if book_menu_choice == 1:
                add_author(authors, library)
            elif book_menu_choice == 2:
                search_authors(authors)
            elif book_menu_choice == 3:
                display_authors(authors)
            elif book_menu_choice == 4:
                break
            else:
                print("\nPlease choose a number between 1-4\n")
        except ValueError:
            print("\nThats not a number! PLease choose a number between 1-4\n")



main()