
with open('/Users/mac/Code/Learning/python-learning/06_files/ap.txt', 'w') as f:
    f.write("Learning Python is fun!")

with open('/Users/mac/Code/Learning/python-learning/06_files/ap.txt', 'w') as f:
    for line in f:
        print(line)
