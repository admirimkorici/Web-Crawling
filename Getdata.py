from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re

open = urlopen("https://www.900gpa.com/en/product/resin/ResinPreg_00EDB4EC83?u=metric")
bsobj = soup(open.read())