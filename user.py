# User Operations:

#         User Operations:
#         1. Add a new user
#         2. View user details
#         3. Display all users


# - Adding a new book with all relevant details.
# - Allowing users to borrow a book, marking it as "Borrowed."
# - Allowing users to return a book, marking it as "Available."
# - Searching for a book by its unique identifier (title) and displaying its details.
# - Displaying a list of all books with their unique identifiers.
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

# User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.

import random

class User:
    def __init__(self, name, email):
        self.name = name
        self.__email = email
        self.__user_id = None
        self.borrowed_books = []
    
    def get_user_id(self):
        return self.__user_id
    
    def get_user_email(self):
        return self.__email
    
    def generate_user_id(self):
        self.__user_id = random.randint(1000, 9999)
        return self.__user_id

user1 = User("Skylar", "S@gmail.com")

print(user1.generate_user_id())
print(user1.get_user_id())
print