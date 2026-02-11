# basic decorator
# def decorator(func):
#     def wrapper():
#         print("I am about to execute a function...")
#         func()
#         print("I have executed the function...")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello")

# say_hello()

# Decorator with args
def repeat(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat(7)
def hello(name):
    print(f"Hello {name}")

hello("Arpit")
