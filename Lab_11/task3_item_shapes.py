import math
class Item:
    def area(self):
        pass
class BookShelf(Item):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Table(Item):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
if __name__ == "__main__":
    items = [BookShelf(19, 30), Table(6.8)]
    for i in items:
        print("Area:", i.area())
