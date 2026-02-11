
class Employee:
    def __init__(self, name):
        self.name = name
    
    @property
    def first_name(self):
        return self.name.split(" ")[0]

    @first_name.setter
    def first_name(self, firstname):
        self.name = firstname + " " + self.name.split(" ")[1]

e = Employee("John Doe")
print(e.first_name, e.name) # first_name param does not exist in the class but using @property decorator, we converted the method to a property name
e.first_name = "Jack" # it should not work as there is not property but using @first_name.setter decorator we used the method to assign the value to a property
print(e.first_name, e.name)
