# Dictionaries

# Two ways to create dictionaries

mydict = dict(name="Yash", age=18, city="Cleveland")
# mydict = {"name":"Yash", "age":18, "city":"Cleveland"}

print(mydict["city"])

# Adding an item
mydict["joke"] = "your mom lol"
print(mydict["joke"])

# Three ways to delete items
del mydict["city"]
# mydict.pop("city")
# mydict.popitem(): Deletes the last item

# Two ways to check and print items
if "age" in mydict:
    print(mydict["age"])

try:
    print(mydict["joke"])
except:
    print("Lol no, this doesn't exist")

# Looping through dictionaries
print()
print("Looping through the dictionary")
for key in mydict:
    print(key)

for value in mydict.values():
    print(value)

print()
print("You can also loop like this:")
for key, value in mydict.items():
    print(key, value)
print()

# Copying a dictionary is similar to copying a list. If done wrong, modifying the copy will also modify the original. (Reference copy)
# To avoid this, copy like this:
mydictcopy = dict(mydict)

# You can also update dictionaries with other ones. For example:
mydict2 = dict(name="Shreya", type="Loser", age=10)

print(str(mydict) + " <-- mydict")
print(str(mydict2) + " <-- mydict2")
print("Updating dict1 using dict2")

mydict.update(mydict2)
print(str(mydict) + " <-- updated mydict")
print()

# You can also use an integer, or even a tuple as a key. Lists however cannot be used as a key, as they are mutable.
ex_tuple = (8, 7)
mydict3 = {ex_tuple: 15}
print(mydict3)
