import sys

# Making a generator
def mygenerator():
    yield 2
    yield 1
    yield 3

# Making a generator object
g = mygenerator()
print(g)

# Going through generator objects
# for i in g:
#     print(i)


# value1 = next(g)
# print(value1)
# value1 = next(g)
# print(value1)
# value1 = next(g)
# print(value1)

a = sorted(g)
print(a)
print()

def countdown(num):
    print("Starting")
    while num > 0:
        yield(num)
        num -= 1

cd = countdown(6)
value2 = next(cd)
print(value2)
value2 = next(cd)
print(value2)
value2 = next(cd)
print(value2)
print()

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Generator objects save a lot of memory...
print("Size of the list object")
print(sys.getsizeof(firstn(1000000)))
print("Size of the generator object")
print(sys.getsizeof(firstn_generator(1000000)))
print()

# A Fibonacci sequence generator:
def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci_generator(1000000)
for i in fib:
    print(i)
print()

# Generator expressions
mygeneratorexpression = (i for i in range(100000) if i % 2 == 0)
mylistexpression = [i for i in range(100000) if i % 2 == 0]

print(sys.getsizeof(mygeneratorexpression))
print(sys.getsizeof(mylistexpression))