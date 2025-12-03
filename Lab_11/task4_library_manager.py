class Librarian:
    def role(self):
        print("Organizing books in the library.")
class Cataloger:
    def role(self):
        print("Cataloging books systematically.")
class LibraryManager(Librarian, Cataloger):
    def role(self):
        super().role()  
        print("Also manages library events and readers.")
if __name__ == "__main__":
    lm = LibraryManager()
    lm.role()
