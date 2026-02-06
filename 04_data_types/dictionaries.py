
marks = {"arpit": 93, "shubham": 90, "anmol": 20}
print(marks)
print(marks['arpit'])

marks['anmol'] = 50
print(marks)

print(marks.keys())
print(marks.values())

marks.pop('shubham')
print(marks)

# dictionary comprehension
dict_comp = {x:x**2 for x in range(1,11)}
print(dict_comp)
