# Lists

mylist = ["banana", "cherry", "apple"]

print(str(mylist) + " <-- mylist")
print(mylist[0] + " <-- the first item in mylist")
print(mylist[-1] + " <-- the last item in mylist. Using -1 as the index shows the last element.")
print()


mylist2 = ["stupid", 5, "aaa", "hello", "loser", "skillissue"]

if 6 in mylist2:
    print("yes")
else:
    print("no")

print(str(mylist2) + " <-- mylist2")

itemremoved = mylist2.pop()
print(str(mylist2) + " <-- mylist2")
print("The item removed from mylist2 is: " + itemremoved + "\n")
mylist2.append(itemremoved)

mylist2.remove(5)
print(str(mylist2) + " <-- mylist2")
print("5 was removed")

mylist2.reverse()
print(mylist2)
print("List was reversed\n")

mylist2.sort()
print(mylist2)
print("List was sorted. Use the sorted() method if you want to sort to a new list.\n")

mylist2.clear()
print(mylist2)

mylist2 = [0] * 5
print(mylist2)
print("mylist2 consists of 5 zeros\n")

mylist3 = mylist2
print(str(mylist2) + " <-- mylist2")
print(str(mylist3) + " <-- mylist3")

mylist3.pop()

print(str(mylist2) + " <-- mylist2")
print(str(mylist3) + " <-- mylist3")
print("Modified mylist3, but both lists got modified. Use .copy(), list(), or [::] to make an actual copy where the lists are distinct.\n")

print("Elegant method of creating new lists from an existing list: ")
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist2 = [i*i for i in mylist1]
mylist3 = [i*i for i in mylist2]
print(str(mylist1) + " <-- mylist1")
print(str(mylist2) + " <-- mylist2")
print(str(mylist3) + " <-- mylist3")