# Sets: no duplicates, and order is arbitrary

set1 = {1, 2, 3, 4, 3, 2, 1}
print(set1)

set2 = set("Hello")
print(set2)

# To create an empty set:
set3 = set()
print(type(set3))

set3.add("Ya mum")
print(set3)

set3.remove("Ya mum")
set3.discard("Hello")
# Discard will remove a member if it exists, otherwise it won't cause an error
# set3.pop() will remove a random member

print()

# Unions and intersections
# Union will combine elements from 2 sets without duplication, intersection will combine elements that occur in both sets

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)
i = odds.intersection(evens)
print(i)
print()

# Difference will take the values in the first set EXCEPT for those that are also present in the second set.

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
diff2 = setB.difference(setA)
print(diff)
print(diff2)

# Symmetric difference will take both sets, and print out elements that aren't common in either set.
# This means that regardless of the order (setA.diff(setB) or setB.diff(setA))), the result is the same.

symdiff = setA.symmetric_difference(setB)
print(symdiff)
print()

# These methods return a new set, they don't modify the existing set. The methods that will modify the set in place are:
# .update() for union, .intersection_update() for intersection, .difference_update() for difference, and
# .symmetric_difference_update() for symmetric difference.

# Subset and superset methods. Kind of self-explanatory, run the code and you will understand
setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}

print(setC.issubset(setD))
print(setD.issubset(setC))
print(setC.issuperset(setD))
print(setD.issuperset(setC))
print()

# Disjoint means that 2 sets are completely different. For example:
setE = {6, 7, 8, 9}
print(setC.isdisjoint(setE))
print(setD.isdisjoint(setE))
print()

# If you want to make actual copies of sets (not reference copies), use the set() method or the .copy() method

# Frozen sets are normal sets, but immutable
frozensetA = frozenset([1, 2, 3, 4])
print(frozensetA)