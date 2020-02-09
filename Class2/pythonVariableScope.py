## Variable Scope and Global statement

# Ex-1
def myfunc():
  x = 300
  print(x)

myfunc()

# Ex-2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()


# Ex-3 Global scope
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# Global Statement
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)