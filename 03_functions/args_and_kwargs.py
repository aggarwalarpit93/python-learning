
# *args is used when there are n number of arguments in the function call and you have no idea the exact number of arguments

def sum(*args):
    # NOTE: *args will be a tuple. So here its value will be (1,2,3,4,5,6) and not a list
    total = 0
    for item in args:
        total += item
    return total

print(sum(1,2,3,4,5,6))

# **kwargs is used to convert the n number of arguments into a dictionary

def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, vikrant=54, jack=34, Marie=90)
