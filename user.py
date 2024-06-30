
# User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
import random

class User:
    def __init__(self, name, email):
        self.name = name
        self.__email = email
        self.__user_id = None
        self.borrowed_books = []
    
    def get_user_id(self): #getter for user_id
        return self.__user_id
    
    def get_user_email(self): #getter for user_email
        return self.__email
    
    def generate_user_id(self): #method to generate a random user_id
        self.__user_id = random.randint(1000, 9999) #generates a random user_id between 1000 and 9999
    
    def assign_book(self, book): #method to assign a book to a user
        self.borrowed_books.append(book) #appends the book to the borrowed_books list
    
    def get_borrowed_books(self): #method to get the borrowed books
        if self.borrowed_books:     #checks if the borrowed_books list is not empty
            for book in self.borrowed_books: #iterates through the borrowed_books list
                print(book.title) #prints the title of the book
        else:
            print("No books found") #prints a message if no books are found

    def remove_book(self, book):
        if book in self.borrowed_books: #checks if the book is in the borrowed_books list
            self.borrowed_books.remove(book) #removes the book from the borrowed_books list
        else:
            print("Book not found in borrowed books.")
    
    
        


# user1 = User("Skylar", "S@gmail.com")

# print(user1.generate_user_id())
# print(user1.get_user_id())
# print