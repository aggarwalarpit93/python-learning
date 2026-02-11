# marks = [12,23,34,45]
# mixed = [12,"Hello",False,4.5]

# print(marks[0])
# print(mixed[3])
# print(marks[1:3])

# marks.append(12)
# marks.pop()
# marks.sort()
# marks.remove(2)

# map method on list
num = [1,2,3,4,5,6,7,8,9]

def square(x):
    return x*x

squareNum = list(map(square, num))
print(squareNum)

#filter method on list
num = [1,2,3,4,5,6,7,8,9]

def is_divisible_by_3(x):
    if x%3 == 0:
        return True
    else:
        return False

squareNum = list(filter(is_divisible_by_3, num))
print(squareNum)
