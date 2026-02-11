
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add_point(self, p):
        return Point((self.x + p.x), (self.y+p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")
    
    def __add__(self, p):
        return Point((self.x + p.x), (self.y+p.y))


p1 = Point(1,2)
p2 = Point(3,4)

# this is one way to add operators
p3 = p1.add_point(p2)
p3.print_point()

# this is new way to add operators
p3 = p1+p2 # 2 objects are added using the __add__ method in the class. There are many more like __sub__, __mul__, __truediv__ etc
p3.print_point()
