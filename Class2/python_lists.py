"""
https://docs.python.org/3/tutorial/datastructures.html

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""


# Create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Accessing a list
print(thislist[1])

# Negative Indexing
print(thislist[-1])

# Listing slicing 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
print(thislist[1::2])


# Change the value of an Item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Loop through a list
for x in thislist:
  print(x)


# Get the length of a list
print(len(thislist))

# Adding Items to list using append() method
thislist.append("orange")
print(thislist)

# Adding Items to list using insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove Item from a list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Items in list using pop(), del and clear() methods
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)