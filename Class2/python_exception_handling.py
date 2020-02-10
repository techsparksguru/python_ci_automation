"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

#Ex-1
try:
  print(x)
except NameError:
  print("Variable x is not defined")
else:
  print("Looks good")


#Ex-2 
try:
  with open("demofile.txt") as f:
    f.write("Lorum Ipsum")
except IOError:
  print("Something went wrong when writing to the file")
finally:
  f.close()


## Raising an exception
#Ex-1
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")   

#Ex-2
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

#Ex-3
