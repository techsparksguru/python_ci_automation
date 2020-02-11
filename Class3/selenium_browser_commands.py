#Import webdriver module from selenium
from selenium import webdriver

# Create a webdriver instance for chrome browser
browser = webdriver.Chrome()

# GoTo (Go to a URL)
browser.get("http://www.seleniumframework.com")
browser.maximize_window()

# Print Browser Name
browser.Name

# Browser Back 
browser.back()

# Browser Forward
browser.forward()

# Refresh Page
browser.refresh()

# Browser Title 
browser.title

# Get Browser Current URL
browser.current_url

# Assert Statements
browser.get("http://www.python.org")
assert "Python" in browser.title

# Quit Browser
browser.quit()

# Close the browser Tab
browser.close()
