

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
        if self.get_availability() == "Availible": # if self.__is_available is Availible we set it to Borrowed
            self.__is_available = "Borrowed"    # else self.__is_available is Borrowed we set it to Availible
        else:
            self.__is_available = "Availible" #returns the availability of the book
        
    
    def borrow_book(self): # method for borrowing a book
        if self.get_availability() == "Availible": #checks if the book is availible
            self.set_availability() #sets the availability to False
            return True #returns True if the book is borrowed
        return False #returns False if the book is not borrowed
    
    def return_book(self): #method for returning a book
        if self.set_availability() == "Borrowed": #checks if the book is borrowed
            self.set_availability() #sets the availability to True
    


# print(book1.get_availability())
# print(book1.borrow_book())
# print(book1.get_availability())
# print(book1.return_book())
# print(book1.get_availability())
# print(book1.title)
# print(book1.author)
# print(book1.genre)
# print(book1.pub_date)


