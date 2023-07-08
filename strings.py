from timeit import default_timer as timer
# Strings: ordered and immutable

# Useful methods and such

stringA = "Hello World"

if "ello" in stringA:
    print("yes")
print()

stringA = "   Hello  World   "
print(stringA)
stringA = stringA.strip()
print(stringA)
print()

# Other methods: .startswith("something"), .endswith("something")
# .find("something") (returns first index of that occurence), .count("something")
# .replace ("thing", "new thing")

# Because strings are immutable, these above methods don't change the string directly, they just return a new one.
# You have to re-assign it to the original string if you want to change it.

# Splitting strings into lists
stringB = "You have a skill issue lol imagine"
print(stringB)
listB = stringB.split()
print(listB)

# The split() method uses a default delimiter (what to split by) as a space. You can set the delimiter as something else in 
# the arguments.

# To go back from a list to a string, use the .join() method shown below.
stringC = '...'.join(listB)
print(stringC)
print()

# .join() is much better than a for-loop. Let's show this.

longlist = ["a"] * 1000000

# Slow, bad code. Creates too many strings (because they are immutable)
longstring = ""
start = timer()
for i in longlist:
    longstring += i
stop = timer()
print(str(stop - start) + " is how long the for-loop took.")

start = timer()
longstring = ''.join(longlist)
stop = timer()
print(str(stop - start) + " is how long the .join() took.")
print()

# Two ways to format strings. The old way is with % or .format(). The new way is with f-strings.
# F-String are cooler. Watch and learn loser.
var = 5.235981
var2 = 74194.36269504372

print("var is %f" % var)
print("var2 is %.3f" % var2)
print()

print("var is {:.2f} and var2 is {}".format(var, var2))

print(f"var is {var:.4f} and var2 is {var2}")
# 69 lines of code, nice.