

# Book: A class representing individual books with attributes such as title, author,  genre, publication date, and availability status

class Book:
    def __init__(self, title, author, genre, pub_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date= pub_date
        self.__is_available = "Availible"

         # getter
    def get_availability(self):
        return self.__is_available
    
    def set_availability(self):
        # if self.__is_available is Availible we set it to Borrowed
        if self.get_availability() == "Availible":
            self.__is_available = "Borrowed"
        # else self.__is_available is Borrowed we set it to Availible
        else:
            self.__is_available = "Availible"
        
    # method for borrowing a book
    def borrow_book(self):
        # if its available then we set use the setter to set it to the opposite which is False
        if self.get_availability() == "Availible":
            self.set_availability()
            return True #returns Availible that we are able to borrow the book
        return False
    
    def return_book(self):
        if self.set_availability() == "Borrowed": #sets the availability back to true if its False
            self.set_availability()


book1 = Book("LOTR", "Tolkien", "Fantasy", 1928)

# print(book1.get_availability())
# print(book1.borrow_book())
# print(book1.get_availability())
# print(book1.return_book())
# print(book1.get_availability())
# print(book1.title)
# print(book1.author)
# print(book1.genre)
# print(book1.pub_date)


