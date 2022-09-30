from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
options = Options()
options.headless = True
while 1:
    driver = webdriver.Firefox(options=options)
    driver.get(
        "https://www.google.com/search?client=firefox-b-1-d&q=python+list+comprehension")
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    url_element = soup.find_all(
        "div", attrs={"data-url": re.compile("^https://")})
    driver.close()
    if url_element != []:
        for url in url_element:
            print(url["data-url"])
        break
