# What is Selenium (python)?

Selenium automates browsers. That’s it! Selenium follows webdriver protocol i.e. http over wire. What that means is – We can execute commands on a browser by passing GET, POST etc. calls from our scripts. Selenium is a library that comes in various programming languages and here we will be using the python bindings for Selenium. Since selenium is a library/module that goes on python runtime, we will install it through pip (pip is probably the most popular way to install libraries in python). Compare this with bundler in Ruby, Maven/Gradle in Java, npm in node.

### Installing, Create and activate the Virtual Environment   
```
pip install virtualenv

mkdir C:\envs\seleniumpractice

virtualenv C:\envs\seleniumpractice

C:\envs\seleniumpractice\Scripts\activate.bat
```

### Installing Selenium via pip
pip install selenium==3.141.0


In This module our focus is on working with Selenium Browser Commands, Finding Elements applying different strategies, Waits in Selenium, Exceptions and so on.