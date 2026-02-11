
class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name of the employee is {self.name}"
    
    # Similar to __str__ but only used by dev for debugging purposes
    def __repr__(self):
        return f"Name: {self.name}"
    
    def __len__(self):
        return len(self.name)

e = Employee("Arpit Aggarwal")
print(e.name)
print(str(e)) # it works via __str__ dunder/magic method
print(repr(e)) # it works via __repr__ dunder/magic method
print(len(e)) # it works via __len__ dunder/magic method

# There are many other magic methods available. Can be checked on the python documentation
