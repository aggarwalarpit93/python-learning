
class Employee:

    company = "HP"

    def __init__(self, name):
        self.name = name
    
    # This is instance methods
    def print_info(self):
        return f"Name is: {self.name}"
    
    # This is static methods because it does not have self as the parameter. It does not change anything on the object
    @staticmethod
    def sum(a, b):
        return a+b
    
    @classmethod
    def change_company_name(cls, new_name):
        cls.company = new_name
    
    

e1 = Employee("John Doe")

print(Employee.company, e1.company) # Both outputs HP
print(e1.print_info()) # prints: name is John Doe

print(e1.sum(1,2)) # prints 3: It works fine only if I add @staticmethod as the decorator
print(Employee.sum(2,3)) # prints 5: It should work fine even if I do not add @staticmethod decorator

e1.change_company_name("Dell")
print(e1.company, Employee.company)

Employee.change_company_name("Acer")
print(e1.company, Employee.company)
