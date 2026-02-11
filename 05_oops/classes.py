
class Employee:

    company = "Tesla"

    def __init__(self, company):
        self.company = company # not compulsory to define variable at top

    def get_salary(self):
        return 1000
    
e = Employee("RMgX tech")
print(e.get_salary())
print(e.company)

e2 = Employee("Google")
print(e2.get_salary())
print(e2.company)

# To print default value of company
print(Employee.company)

