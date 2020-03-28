import time
from selenium import webdriver

# Function that prints the html tag of all the links (<a> tags) on the website. Default webpage is: https://www.inmar.com
def extract_links(url="https://www.inmar.com"):
    browser = webdriver.Chrome()
    browser.get(url)
    print(browser.title)

    valid_links = []
    mail_addresses = []
    broken_links = []
    
    for links in browser.find_elements_by_xpath('.//a'):
        if(str(links.get_attribute('href')).startswith("https:")):
            # appending valid links into valid_links list
            valid_links.append(links.get_attribute('href')) 

        elif("@" in str(links.get_attribute('href'))):
            # appending mail_addresses into mail_addresses list
            mail_addresses.append(links.get_attribute('href'))

        else:
            # collecting broken links
            broken_links.append(links.get_attribute('href'))
            
            
    print("\nBelow are the valid links on the webpage:")
    # Picking the unique links from the valid_links list
    valid_links=list(set(valid_links))
    for x in valid_links:
        print(x)

    print("\nBelow are the mail addresses on the webpage:")
    for x in mail_addresses:
        print(x)

    print("\nTotal number of links on the webpage are :  " + str(len(valid_links) + len(mail_addresses)))
    browser.quit()

extract_links(url="http://automationpractice.com/index.php?controller=authentication&back=my-account")