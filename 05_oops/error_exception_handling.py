
while True:
    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        if num1 < 1 or num2 < 1:
            raise ValueError("Please do not use 0")
        sum = num1 + num2
        print(f"Sum of 2 numbers is: {sum}")

    except ValueError as e:
        print(e)

    except ZeroDivisionError:
        print("Do not enter 0")

    except Exception as e:
        print("Some error occured", e)

    # Only runs if there is no error
    else:
        print("Everything is working fine.")

    # Runs everytime even if there is error or no error
    finally:
        print("You are done")
