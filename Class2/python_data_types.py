"""
https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747

##Mutable objects: A mutable object can be changed after it is created
list, dict, set, byte array

## Immutable objects:
int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

# Integers
integer_a = 10
integer_b = 20
print(integer_a + integer_b)

# Strings
string_a = "abc"
string_b = "bcd"
print(string_a + string_b)

# Floats
float_a = 10.1
float_b = 20.1
print(float_a + float_b)

# Float Comparison
print(integer_a==integer_b)

# Lists
strings_list = ["abc","def","xyz"]
ndim_list = [[1,2],[3,4]]
list_items = [1,"Suhas", [5,6], {"Lesson1":5, "Lesson2":25}]
print(strings_list)
print(ndim_list)
print(list_items)

# Tuples
strings_tuple = ("abc","def","xyz")
ndim_tuple = ((1,2),(13,41))
list_tuple = (1,"Suhas", [5,6], {"Lesson1":5, "Lesson2":25})
print(strings_tuple)
print(ndim_tuple)
print(list_tuple)

# Dictionary
person_dict = {"name": "Joe", "age": 35, "job": "plumber"}
print(person_dict)

# Sets
my_list = [1, 2, "John", "John", 2, 1, 5, 6, 8, 9, 8]
set(my_list)

# Bool
a = False
b = True
a == b

bool(0)
bool(10)
bool("a")