import requests
from bs4 import BeautifulSoup
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python%2CDjango&txtLocation=').text
print(html_text)