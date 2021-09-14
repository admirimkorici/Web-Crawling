import requests
from bs4 import BeautifulSoup
html_text = requests.get('https://www.900gpa.com/en/search?p=resin&u=metric&refinements%5BproductInformation.matrixType%5D%5B0%5D=Thermoset&refinements%5BproductInformation.resinType%5D%5B0%5D=BMI&uid=ResinPreg_00EDB4EC83').text
soup = BeautifulSoup(html_text, 'lxml')

tables = soup.find()
print(tables)
