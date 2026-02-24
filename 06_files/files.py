
# Read file
# f = open('/Users/mac/Code/Learning/python-learning/06_files/ap.txt', 'r')
# content = f.read()
# print(content)
# f.close()

# Read file line by line
f = open('/Users/mac/Code/Learning/python-learning/06_files/ap.txt', 'r')
for line in f:
    print(line)
f.close()

# new example of reading the file
with open('/Users/mac/Code/Learning/python-learning/06_files/ap.txt', 'r') as f:
    content = f.read()
    print(content)
    # No need to close as it is already handled by with attribute

# Write to a file
# f = open('/Users/mac/Code/Learning/python-learning/06_files/empty.txt', 'w')
# string = '''
# This as the empty file. but now I am adding this content to the file.
# '''
# f.write(string)
# f.close()

# Append to a file
# f = open('/Users/mac/Code/Learning/python-learning/06_files/ap.txt', 'a')
# string = '''
# I am expert in Laravel.
# '''
# f.write(string)
# f.close()

