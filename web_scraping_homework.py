import requests
import bs4
import timeit
from collections import Counter
# url=requests.get("http://quotes.toscrape.com/page/1/")
# requests.models.Response
# soup=bs4.BeautifulSoup(url.text,"lxml")
# authors=soup.select(".author")
# x=[]
# for i in author:
#     x.append(i.text)
# # print(set(x))
# quotes=soup.select(".text")
# # y=[]
# # for i in quotes:
# #     y.append(i.getText())
# # for i in y:
#     print(i)

# tags=soup.select(".tag-item")
def all_authors():
    unic_authors=[]
    for n in range(1,20):
        parsing_url=requests.get(f"http://quotes.toscrape.com/page/{n}/")
        soup=bs4.BeautifulSoup(parsing_url.text,"lxml")
        authors=soup.select(".author")
        quotes=soup.select(".text")
        while len(quotes)!=0:
            for author in authors:
                unic_authors.append(author.text)
            break
    return unic_authors
x=Counter(all_authors()).most_common()

for i in reversed(x):
    print(i)





