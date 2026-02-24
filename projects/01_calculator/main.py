
try:
    num1 = int(input("Enter the first number: \n"))
    num2 = int(input("Enter the second number: \n"))
    
    operation = input("What kind of operation you want to perform? Ex. add,sub,mul,div \n")
    
    match operation:
        case 'add':
            print(f"Sum of 2 numbers is: {num1+num2}\n")
        case 'sub':
            print(f"Diff of 2 numbers is: {num1-num2}\n")
        case 'mul':
            print(f"Multiplication of 2 numbers is: {num1*num2}\n")
        case 'div':
            print(f"division of 2 numbers is: {num1/num2}\n")
        case _:
            print("Invalid selection of operation\n")

except Exception as e:
    print("Some error occured\n")

