import requests
from bs4 import BeautifulSoup
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')

tables = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
print(tables)
