# Meth uhhhhhhh I mean math...
print(5 * 7)
print(2 ** 4)
print()

# Making repeated items fast
zeros = [0, 1] * 10
print(zeros)

ABstring = "AB" * 10
print(ABstring)
print()

# Use case for *args and **kwargs
# For example, enforcing only keyword arguments

# Unpacking lists/dictionaries for function arguments

def foo(a, b, c, d):
    print(a, b, c)

my_list = [1, 2, 3, 4]
foo(*my_list)
print()

beginning, *middle, last = my_list
print(beginning)
print(middle)
print(last)
print()

# Merging iterables

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)
# Also works with dictionaries