from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
annoyingString = "aaaaabbbbbbcccccdddddddddddeeeeffghhhhiiiiiiiii"

# This thing is magic, watch this:
annoyingStringCounter = Counter(annoyingString)
print(annoyingStringCounter)
print("That is a dictionary")
print()
print(annoyingStringCounter.items())
print("Those are key-value pairs, a list")
print()
print(annoyingStringCounter.keys())
print(annoyingStringCounter.values())
print("Keys and values list")
print()

# The .most_common() method returns a list with tuple(s), the argument signifying the number of most common elements to return
print(annoyingStringCounter.most_common(4))
print(annoyingStringCounter.most_common(4)[0])
print(annoyingStringCounter.most_common(4)[0][0])
print(annoyingStringCounter.most_common(4)[0][1])
print("The .most_common() method")
print()

# Turning the counter into a list
print(list(annoyingStringCounter.elements()))


# Now the namedTuple, pretty simple
Point = namedtuple('Point', 'x, y, z')
pt = Point(10, 4, -2)
print(str(pt) + " --- x-point is: " + str(pt.x))
print()

# Now Ordered Dictionaries
# Actually these are kind of irrelevant after 3.6, as normal dictionaries now remember their order anyways...


# Now Default Dictionaries
# Default dictionaries will set a default value if it has not been specified for a given key
# If you tried printing the value for a key that has not been set, a normal dictionary would return an error

d = defaultdict(int)
d ['a'] = 1
d ['f'] = 3
print(d['a'])
print(d['b'])
print(d['l'])
print("Printed default values")
print()


# Finally, a deque. Basically a double-ended queue.
deque_var = deque()

deque_var.append(1)
deque_var.append(2)
deque_var.appendleft(3)
deque_var.appendleft(4)

print(deque_var)

deque_var.extend([6, 2, 9, 8])
print(deque_var)

deque_var.extendleft([99, 83])
print(deque_var)
print()

# Moves all elements (argument) number of times to the right. Use a negative number to move to the left.
deque_var.rotate(1)
print(deque_var)