import requests
import bs4
import timeit
from collections import Counter
url=requests.get("https://kalinaphotolab.com")
requests.models.Response
soup=bs4.BeautifulSoup(url.text,"lxml")
logo=soup.select("d")
x=[]
for i in logo:
    print(i)