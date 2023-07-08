import random
import secrets
import numpy as np

# Random number between 0 and 1
a = random.random()
print(a)

# Random number between 1 and 10
a = random.uniform(1, 10)
print(a)

# Random number between 1 and 10 NOT INCLUDING 10
a = random.randrange(1, 10)
print(a)

# Random number in a distribution with mu and sigma (mean and standard deviation)
a = random.normalvariate(0, 1)
print(a)
print()

# Pick a item from a list
mylist = list("ABCDEFG")
print(mylist)
a = random.choice(mylist)
print(a)

# Pick multiple random items from a list, without repeats
a = random.sample(mylist, 3)
print(a)

# Pick multiple random items from a list, with repeats
a = random.choices(mylist, k=3)
print(a)

# Shuffle a list
random.shuffle(mylist)
print(mylist)
print()

# How to reproduce data multiple times
random.seed(1)
print(random.random())
print(random.randint(1, 10))
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
print()

# Because of this, it is not recommended to use this module for security purposes. For that, there exists the "secrets" module.
# ooooooooo secretsssssssssssssssssssssssss
# Disadvantage, the secrets module uses algorithms that take longer times, but it generates true random numbers

# Random number between 0 and (argument), not including (argument)
b = secrets.randbelow(10)
print(b)

# Random integer that uses (argument) bits. If you use 4, then it can be from 0 to 15
b = secrets.randbits(4)
print(b)

# Random items from a list
mylist2 = list("ABCDEFG")
b = secrets.choice(mylist)
print(b)
print()

# Using numpy to make random lists
b = np.random.rand(3)
print(b)
print()

b = np.random.rand(3, 3)
print(b)
print()

# randint is exclusive of the higher number argument
b = np.random.randint(0, 10, 3)
print(b)
print()

b = np.random.randint(0, 10, (3, 4))
print(b)
print()

# If you have a numpy array, and use the shuffle() method, notice that it shuffles only on one axis:
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print()
np.random.shuffle(arr)
print(arr)

# Also, the numpy and random seed generators are different.