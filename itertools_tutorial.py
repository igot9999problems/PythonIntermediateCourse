from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat

# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# Vietnam flashback to AP Stats...
# PTSD: Post Tramautic Stats Disorder

a = [1, 2]
b = [3, 4]

# Products
print("Products:")
prod = product(a, b)
print(prod)
print(list(prod))

prod = product(a, b, repeat = 2)
print(list(prod))
print()

# Permutations
print("Permutations:")
c = [1, 2, 3]
perms = permutations(c)
print(list(perms))
perms = permutations(c, 2)
# Second argument specifies the length of each permutation (The choose variable, r)
print(list(perms))
print()

# Combinations, without and with replacement
print("Combinations:")
d = [1, 2, 3, 4]
combs = combinations(d, 2)
# Second argument specifies the length of each combination (The choose variable, r). Argument is mandatory.
print(list(combs))
print()

print("Combinations with Replacement:")
combs_wr = combinations_with_replacement(d, 2)
print(list(combs_wr))
print()

# Accumulate
print("Accumulate:")
e = [1, 2, 3, 4, 5, 6, 7]
acc = accumulate(e)
print(e)
print(list(acc))
# You can also multiply or do other functions, not just addition. You need to import operator for this, then do this:
acc = accumulate(e, func=operator.mul)
print(list(acc))
print()

f = [1, 2, 6, 5, 3, 5, 7, 8, 6]
print(f)
acc = accumulate(f, func=max)
print(list(acc))
print()

# The groupby function
print("GroupBy Function:")

def smaller_than_three(x):
    return x < 3

g = [1, 2, 3, 4, 5, 6, 7, 8, 8]

group_obj = groupby(g, smaller_than_three)
for key, value in group_obj:
    print(key, list(value))
print()

group_obj = groupby(g, lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))
print()

# The above 2 blocks of code are the same

# Using the element itself as the key function

h = [1, 2, 3, 4, 4, 5, 4, 6, 7, 8]
group_obj = groupby(h)
for key, value in group_obj:
    print(key, list(value))
print()

# A more epic example of the groupby function
humans = [{"name":"Yash", "age":18}, {"name":"Shaishav", "age":16}, {"name":"Navya", "age":16}, {"name":"Kedar", "age":18},
          {"name":"Aayus", "age":16}]
group_obj = groupby(humans, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))
print()
# Kind of. The groupby function only collect contiguous items, items that are next to each other. This is why Shaishav and Navya 
# are grouped together, but me and Kedar aren't, and neither is Aayus.

# Infinite Iterators
print("Infinite Iterators:")
for i in count(10):
    print(i)
    if i == 20:
        break

j = [1, 2, 3]
# for i in cycle(j):
#     print(i)

for i in repeat(1, 9):
    print(i)