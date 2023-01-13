import pandas as pd
from selenium import webdriver
import lxml

url = "https://www.greatschools.org/rhode-island/providence/schools/?view=table"

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source

table = pd.read_html(html)
df = table[0]

driver.close()

print(df)
