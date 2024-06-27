# Author Operations:

#         Author Operations:
#         1. Add a new author
#         2. View author details
#         3. Display all authors

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

class Author:
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio
        pass

    def display_author():
        print\
        




books = [] 
authors = []
# assuming books is a list of book objects
for book in books:
    for author in authors:
        if book.author == author.name:
            print(f"Author: {author.name} Biography: {author.biography}")