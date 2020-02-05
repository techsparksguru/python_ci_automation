a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# String Slicing
b = "Hello, World!"
print(b[2:5])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])


# String Length
a = "I love watching Cricket"
print(len(a))


# String Methods:
## https://docs.python.org/3/library/stdtypes.html#string-methods

## strip()
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

## lower()
a = "Hello, World!"
print(a.lower())

## upper()
a = "Hello, World!"
print(a.upper())

## replace()
a = "Hello, World!"
print(a.replace("H", "J"))


# String Concatenation

## Ex-1
a = "Hello"
b = "World"
c = a + b
print(c)


## Ex-2 -- Failure Case
age = 36
txt = "My name is John, I am " + age
print(txt) 