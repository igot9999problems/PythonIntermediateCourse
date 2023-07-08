from functools import reduce

# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

def add10_func(x):
    return x + 10
print(add10_func(5))

# The above 2 blocks of code are the same

# Multiple arguments for a lambda function
mult = lambda x, y: x * y
print(mult(6, 9))
print()

# Lambda functions used as arguments in other functions

def sort_by_y(x):
    return x[1]

print("Lambda functions used as arguments in other functions:")
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sortedx = sorted(points2D)
points2D_sortedy = sorted(points2D, key=lambda x: x[1])
# points2D_sortedy = sorted(points2D, key=sort_by_y) is the same as the above line
print(points2D)
print(points2D_sortedx)
print(points2D_sortedy)
print()

points2D_sortedsum = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sortedsum)
print()

# Map function, map(func, iterable)
print("Map functions:")
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)
b_copy = [x * 2 for x in a]
print(a)
print(list(b))
print(b_copy)
print()

# Filter function, filter(func, iterable)
print("Filter functions:")

c = filter(lambda x: x % 2 == 0, a)
c_copy = [x for x in a if x % 2 == 0]
print(list(c))
print(c_copy)
print()

# Reduce function, import reduce from functools
print("Reduce function:")
reduce_a = reduce(lambda x, y: x * y, a)
print(reduce_a)