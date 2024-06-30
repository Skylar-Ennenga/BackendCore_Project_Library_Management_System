# User Operations:

#         User Operations:
#         1. Add a new user
#         2. View user details
#         3. Display all users

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
    
    def assign_book(self, book):
        self.borrowed_books.append(book)
    
    def get_borrowed_books(self):
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(book.title)
        else:
            print("No books found")

    def remove_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("Book not found in borrowed books.")
    
    
        


# user1 = User("Skylar", "S@gmail.com")

# print(user1.generate_user_id())
# print(user1.get_user_id())
# print