class Library:
    def info(self):
        print("Welcome to the library. We have many books available.")

class Book(Library):
    def info(self):
        print("This book contains exciting stories and valuable knowledge.")

class Librarian(Library):
    def info(self):
        print("The librarian helps visitors find the books they need.")

lib = Library()
novel = Book()
staff = Librarian()

lib.info()
novel.info()
staff.info()
