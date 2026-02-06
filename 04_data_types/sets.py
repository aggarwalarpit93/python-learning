
# Sets cannot have repeated elements and is unordered
# sets = {"a", "b", "c"} # it is correct
sets = {"a", "b", "c", "c"} # it is incorrect. C will be printed only once
sets.add("e") # since sets are unordered, e is addd randomly in the set
sets.remove("a")
sets.pop() # remove random element from set

print(sets)

# print(sets[1]) # throws an error

new_set = {"a", "p", "q", "r"}

print(sets.union(new_set))
print(sets.intersection(new_set))
print(sets.difference(new_set))
