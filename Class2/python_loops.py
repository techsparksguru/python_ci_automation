"""
Python has two primitive loop commands:

while loops
for loops

https://docs.python.org/3/tutorial/controlflow.html
"""

## While Loops
# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1


# Exit the loop when i is 3 using break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


## For Loops and Range function

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Loop through a string
for x in "banana":
  print(x)


# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# range() function

# Ex-1
for x in range(6):
  print(x)

# Ex-2
for x in range(2, 6):
  print(x)

# Ex-3
for x in range(2, 30, 3):
  print(x)


## Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# Print number pattern 
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')