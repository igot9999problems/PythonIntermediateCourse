import copy

# Shallow copy: One level deep, only references of nested child objects
# Deep copy: Full independent copy

original = [0, 1, 2, 3, 4, 5]
cpy = original
cpy[0] = -10
print(original)
print(cpy)
print()
# The original also got modified. Instead...

original = [0, 1, 2, 3, 4, 5]
cpy = copy.copy(original)
cpy[0] = -10
print(original)
print(cpy)
print()
# Better. But what about nested objects?

original = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
cpy = copy.copy(original)
cpy[0][0] = -10
print(original)
print(cpy)
print()
# Because original is a nested list, and shallow copies are only one level deep, the copy method only goes one level deep, 
# and because of this, python just makes cpy a reference to the same object that original is referencing. Instead...

original = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
cpy = copy.deepcopy(original)
cpy[0][0] = -10
print(original)
print(cpy)
print()

# This also works for custom objects, it is not limited to the built-in types