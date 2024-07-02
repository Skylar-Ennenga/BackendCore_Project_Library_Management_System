

# Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status

class Book: #class for the book
    def __init__(self, title, author, genre, pub_date): #constructor for the book
        self.title = title 
        self.author = author
        self.genre = genre
        self.pub_date= pub_date
        self.__is_available = "Availible"

         # getter
    def get_availability(self): #method to get the availability of the book
        return self.__is_available
    
    def set_availability(self):
        if self.get_availability() == "Availible": # __is_availible is set to "Availible"
            self.__is_available = "Borrowed"    #Set it to Borrowed
        else:
            self.__is_available = "Availible" # If it is already set to borrowed set it back to "Availible"
        
    
    def borrow_book(self): # method for borrowing a book
        if self.get_availability() == "Availible": #checks if the book is availible
            self.set_availability() #sets the availability to Borrowed
            return True # returns true that it can be baorrowed
        return False #returns false if it cannot be borrowed
    
    def return_book(self): #method for returning a book
        if self.set_availability() == "Borrowed": #checks if the book is borrowed
            self.set_availability() #sets the availability back to Availible
    



