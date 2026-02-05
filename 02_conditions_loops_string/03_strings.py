
# Print string in 3 ways
# name = "Arpit"
# name = 'Arpit'
# name = '''Arpit is
# a
# developer'''
# print(name)

# Indexing in string
# name = "Arpit"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[-2])

# slicing in string
# name[starting index:end index+1:skip n-1 char]
# name = "Arpit Aggarwal"
# print(name[0:5])
# print(name[6:-1])
# print(name[6:-1:2])
# print(name[:14])
# print(name[0:])
# name[0] = "R" # it is invalid and not allowed

# String Methods
# Note: Original string does not change... It returns new string only
# name = "arpit Aggarwal"
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.find("Aggarwal"))
# print(name.replace('arpit', 'prachi'))
# print(name.split(' ')) # Opposite of split is join

# String formatting and f-string format
template = "Dear {}, you are awesome. Take this {}$ bag."
a = "Arpit"
a1 = 1000

s1 = template.format(a, a1) # this is string formatting. Old method
print(s1)

print(f"Dear {a}, you are awesome. Take this {a1}$ bag.") # this is f-string. New method
