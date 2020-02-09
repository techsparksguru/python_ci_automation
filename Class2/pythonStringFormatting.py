# Older Approach

'''
Formatter specifiers:

Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

Useful Resources: 
https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36
https://www.learnpython.org/en/String_Formatting
'''

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# This prints out: The numbers are 5 and 6.46
number1 = 5
number2 = 6.875949
print("The numbers are %d and %.2f" % (number1, number2))

errno = 50159747054
name = 'Bob'
print('Hey %s, there is a 0x%x error!' % (name, errno))


# Using .Format Approach
print("{}, A computer science portal for geeks.".format("GeeksforGeeks"))
print("Every {} should know the use of {} {} programming and {}".format("programmer", "Open", "Source", "Operating Systems")) 
print("Every {2} should know the use of {3} {0} programming and {1}".format("programmer", "Open", "Source", "Operating Systems")) 
print("{gfg} is a {0} science portal for {1}".format("computer", "geeks", gfg="GeeksforGeeks")) 


# String Interpolation / f-Strings(Python 3.6+)
# Ex-1
name = 'Suhas'
f'Hello, {name}!'

# Ex-2
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}.'

# Ex-3
f"Hey {name}, there's a {errno:#x} error!"