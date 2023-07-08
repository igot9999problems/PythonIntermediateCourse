# Errors and Exceptions

# How to raise an exception
a = 5
if a < 0:
    raise Exception('a should be positive')

b = 2
assert (b >= 0), 'b is not positive'

try:
    c = 5 / 1
    d = c + 1
except ZeroDivisionError as e:
    print("You can't divide by 0 you dum dum. Thankfully the rest of your code should still work.")
    print(e)
    # It is good practice to specify the error you are looking for, not just an except statement
except TypeError as e:
    print("You really just tried adding incompatible types you child")
    print(e)
else:
    print("Congratulations, you wrote code that works! Very rare indeed.")
finally:
    print("Cleaning up...")
    print()


# Defining your own exception...
class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooLowError("Value is too low", x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message + ": " + str(e.value))