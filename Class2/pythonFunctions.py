"""
https://www.tutorialspoint.com/python3/python_functions.htm
https://docs.python.org/3/library/functions.html
https://realpython.com/documenting-python-code/
"""

# Creating a function
def my_function():
  print("Hello from a function")


# Calling a Function
my_function()

## Functions with arguments/Parameters
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Multiple arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Passing value to the arguments in the calling function
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


## Functions with default parameter values
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Return Statement
def my_function(x):
  return 5 * x

print(my_function(3))