**Lab 11: Inheritance and Polymorphism in Python**



**Objective:** The purpose of this lab is to practice inheritance, method overriding, polymorphism, and multiple inheritance in Python using library and book examples.



**Tasks:**

1. **Person and Reader classes:** The Person base class has attributes name and age. The Reader class inherits from Person and adds reader\_id. The display\_info() method is overridden to show the reader's ID. This demonstrates inheritance and method overriding.
2. **Library, Book, and Librarian:** The Library base class has an info() method. Book and Librarian classes override it to display different messages. This demonstrates polymorphism.
3. **Item, BookShelf, and Table:** The Item base class defines an area() method. BookShelf and Table override it to calculate specific areas. Calling area() on a list of objects shows runtime polymorphism.
4. **Librarian, Cataloger, and LibraryManager:** LibraryManager inherits from both Librarian and Cataloger. The super() function calls the first parent's method, then additional actions are executed. This demonstrates multiple inheritance and method resolution order.
