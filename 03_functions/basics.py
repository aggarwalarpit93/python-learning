
# Function definition must exist before calling it
# def average(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)

# average(1,2,3)
# average(4,5,6)
# average(c=9,a=7,b=8)

# Lambda Functions
# lambda functions are the single line functions
# square = lambda x: x*x # x is the parameter received in the function
# sum = lambda x,y: x+y
# print(square(4))
# print(sum(2,3))

# Recurssion function
# printing fibonacci series
num = int(input("Enter the fibonacci series length"))
i=2
a = 0
b = 1
print(a)
print(b)
# while(i<num):
#     c = a+b
#     print(c)
#     a = b
#     b = c
#     i += 1

def fibonacci(a,b):
    c = a+b
    print(c)
    a = b
    b = c
    global i # tell to update i value of global variable
    i += 1
    if(i<num):
        fibonacci(a,b)


fibonacci(a,b)
