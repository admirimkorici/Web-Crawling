from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()
url = 'https://www.900gpa.com/en/search?p=resin&u=metric&refinements%5BproductInformation.matrixType%5D%5B0%5D=Thermoset&refinements%5BproductInformation.resinType%5D%5B0%5D=BMI&uid=ResinPreg_00EDB4EC83'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content = soup.find_all('table')

dictionary = dict()
for con in content:
    title = con.h4.text
    element = con.find_all('tr')
    dict1 = dict()
    for con2 in element:
        if con2.th == None:
            print('none')
        else:
            info_title = con2.th.text
            info = con2.td.text.replace('°', 'Grad ')
            dict1[info_title] = info
            dictionary[title] = dict1

with open('C:/Users/user/OneDrive/Documents/Visual Studio Code/Python/Grid Coding/Web Crawling/Data_in_json.json', 'w') as out:
    json_obj = json.dump(dictionary, out, indent=4)
    out.close()
