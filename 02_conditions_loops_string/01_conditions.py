# If-Else conditions
age = 34
if(age > 18):
    print("you can drive")
elif(age == 18):
    print("Let's schedule an interview")
else:
    print("You cannot drive")

# Match statements
num=1
match(num):
    case 1:
        print("value is 1")
    case 2:
        print("value is 2")
    case 3:
        print("value is 3")
    case _:
        print("value does not match")