import functools

# Decorators are a way to extend the functionality/behavior of a function that already exists

# Example, a start_end_decorator:
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

# By adding the line below, you don't need to do: print_name_extended = start_end_decorator(print_name),
# You can directly use the original function name
@start_end_decorator
def print_name():
    print("Yash")

# print_name_extended = start_end_decorator(print_name)
# print_name_extended()

print_name()
print()

# Another function using the start_end_decorator
@start_end_decorator
def your_mom():
    print("Your mom")

your_mom()
print()

# What if your original (inner) function has arguments that it uses? Then this is how you setup the decorator function:
# Use the @functools line before the wrapper to preserve the information of the original function documentation

def start_end_decorator_2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting")
        result = func(*args, **kwargs)
        print("Ending")
        return result
    return wrapper

@start_end_decorator_2
def add5(x):
    return x + 5

result = add5(10)
print(result)
print()

# We will learn later why (and what) *args and **kwargs do, but for now, just know that this is needed

# The help() function in python is used to get the details of modules, classes, functions, etc
# Let's say we have a function that is the same as our add5() function, but it doesn't use a decorator
# Look at what the help() function prints out for the add5_nondecorated() and for add5()

def add5_nondecorated(x):
    return x + 5

print(help(add5_nondecorated))
print(add5_nondecorated.__name__)
print()

print(help(add5))
print(add5.__name__)
print()

# The problem is that python is getting confused about the identity of the add5 function. We want it to print out the same thing 
# that it prints out for the add5_nondecorated.
# To fix this issue, look at the comments pertaining to this in the start_end_decorator_2 function


# That was a lot of stuff to learn, so here's a template for decorators that you can use

def template_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("What you want to happen before")
        result = func(*args, **kwargs)
        print("What you want to happen after")
        return result
    return wrapper

@template_decorator
def template_function(x):
    return x * 5

# print(template_function(10))
# print()

# How do you make repeating decorators?
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Yash")
print()

# Now, nested decoraters. As if decorators themselves weren't already enough.

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

def start_end_decorator_4(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting")
        result = func(*args, **kwargs)
        print("Ending")
        return result
    return wrapper

@debug
@start_end_decorator_4
def say_hello(name):
    print(f"Hello Mr/Mrs {name}")
    return(f"Hello Mr/Mrs {name}")

print(say_hello("Shreya"))
print()

# Lastly, class decorators

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This has executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello_3():
    print("Hello")

say_hello_3()
say_hello_3()
print()

# Some use cases for decorators:
# Implement a timer decorator to find the execution time of a function
# Use a debug decorator (as you've seen) to print info about the called function and it's arguments
# Use a check decorator to see if the arguments satisfy some requirements
# Some more stuff that I don't understand/don't see the use case for