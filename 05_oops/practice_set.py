from time import time

# Problem 1: Write a decorator that prints string before calling the function
# def logger(func):
#     def wrapper(str):
#         print("function is being called")
#         func(str)
#     return wrapper

# @logger
# def say_hello(str):
#     print(str)
    
# say_hello("Hello!")

# Problem 2: Write a decorator that calculates the time takes to execute a function

# def timer(func):
#     def wrapper():
#         t1 = time()
#         func()
#         t2 = time()
#         print(f"Time taken is: {t2-t1}")
#     return wrapper

# @timer
# def sum():
#     total = 0
#     for i in range(1000000):
#         total += i
#     print(total)

# sum()

# Problem 3: Create a getter and setter to set the value of salary and get its values

class Employee:
    
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if(int(salary)<100):
            print("Salary cannot be lower than 100")
        else:
            self._salary = salary

e = Employee(123)
print(e.salary)
e.salary = "12"
print(e.salary)
