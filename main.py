import requests
from bs4 import BeautifulSoup
html_text = requests.get('https://www.900gpa.com/sitemap.xml').text
soup = BeautifulSoup(html_text, 'lxml')

tables = soup.find_all('url')
print(tables)
