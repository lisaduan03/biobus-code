# import requests
# from bs4 import BeautifulSoup

# url = "https://www.greatschools.org/rhode-island/providence/schools/"
# page_response = requests.get(url)
# content = BeautifulSoup(page_response.text,"html.parser")

# table=content.find_all('table')
# table

# import pandas as pd
# from selenium import webdriver

# url = "https://www.greatschools.org/new-york/new-york/schools/?tableView=Overview&view=table"

# driver = webdriver.Chrome()
# driver.get(url)

# html = driver.page_source

# table = pd.read_html(html)
# df = table[0]

# driver.close()

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def webscrape_table():
    url = "https://www.greatschools.org/new-york/new-york/schools/?tableView=Overview&view=table"
    driver = webdriver.Chrome()
    driver.get(url)
    # Wait for the table to load
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "js-search-results"))
    )
    # Extract the table element
    table = driver.find_element_by_id("js-search-results")
    # Pass the table element to pandas' read_html() function
    df = pd.read_html(table.get_attribute('outerHTML'))[0]
    driver.quit()
    return df


import selenium
print(selenium.__version__)

webscrape_table()

