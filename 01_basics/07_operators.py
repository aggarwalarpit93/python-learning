a = 10
b = 2

# arithmetic operators
# print("a + b = ", a + b)
# print("a - b = ", a - b)
# print("a * b = ", a * b)
# print("a / b = ", a / b)
# print("a % b = ", a % b)
# print("a // b = ", a // b)
# print("a ** b = ", a ** b)

# walrus operator :=
# It is used to call a function and assign its value to a variable while it is called inside a function or condition etc

while(data := input("Enter the value: ")):
    if(data == "q"):
        break

    print(data)
