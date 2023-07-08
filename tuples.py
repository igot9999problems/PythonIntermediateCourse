import sys
import timeit

# Tuples are lists, except immutable. So they're basically stubborn lists.
# They support (I think) most of the same functions that lists do.

mytuple = tuple(["Yash", 18, "Cleveland"])
# Or mytuple = ("Yash", 18, "Cleveland") or mytuple = "Yash", 18, "Cleveland"

# To create a tuple with one element, use this syntax (otherwise python will see it as a string/int/whatever instead of a tuple):
# mytuple = ("Blah",)

mytuple2 = ('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
print(mytuple2)
print("")

print(mytuple2.count('i'))
print("Counted the number of occurences of the letter 'i' in mytuple2\n")

print(mytuple2.index('i'))
print("First index occurence of the letter i\n")

mylist = list(mytuple2)
print(mylist)
print("Converted the tuple into a list\n")

# Unpack elements in a tuple to variables. Number of elements and variables must be the same.
name, age, city = mytuple
print("Unpacking mytuple into variables")
print(name)
print(age)
print(city + "\n")

# Also can unpack multiple elements into a list variable using the * operator
i1, i2, *i3, i4, i5 = mytuple2
print("Unpacking multiple elements into a list")
print(i1)
print(i2)
print(i3)
print(i4)
print(i5 + "\n")

# Comparing efficiency of tuples vs lists
mylist3 = [0, 1, 2, "hello", True]
mytuple3 = (0, 1, 2, "hello", True)
print("Size of list is: " + str(sys.getsizeof(mylist3)) + " bytes")
print("Size of tuple is: " + str(sys.getsizeof(mytuple3)) + " bytes")

print("Time to create the list: " + str(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) + " seconds")
print("Time to create the tuple: " + str(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) + " seconds")