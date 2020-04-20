import time
from selenium import webdriver

# Function that prints the html tag of all the links (<a> tags) on the website.
def extract_links(url="https://www.seleniumframework.com"):
    browser = webdriver.Chrome()
    browser.get(url)
    print(browser.title)

    links = []
    
    for link in browser.find_elements_by_xpath('.//a'):
        if(str(link.get_attribute('href')).startswith("https:")):
            # appending valid links into valid_links list
            links.append(link.get_attribute('href')) 
             
    print("\nBelow are the links on the webpage:")
    # Picking the unique links from the valid_links list
    links=list(set(links))
    for x in links:
        print(x)

    print("\nTotal number of links on the webpage are :  " + str(len(links)))
    browser.quit()

extract_links(url="http://automationpractice.com/index.php?controller=authentication&back=my-account")