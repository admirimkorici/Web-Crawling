from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.900gpa.com/en/search?p=resin&u=metric&refinements%5BproductInformation.matrixType%5D%5B0%5D=Thermoset&refinements%5BproductInformation.resinType%5D%5B0%5D=BMI&uid=ResinPreg_00EDB4EC83'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
content = soup.find_all('table')

for con in content:
    title = con.h4.text
    print(title)

#searchbox = driver.find_element_by_xpath('//*[@id="search"]')
#searchbox.send_keys('MrBeast')

#searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
#searchbutton.click()