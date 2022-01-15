import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
isbn = input("ISBN을 입력하세요 : ")
url = "https://www.aladin.co.kr/shop/usedshop/wc2b_search.aspx?ActionType=1&SearchTarget=Book&KeyWord={}&x=34&y=28".format(isbn)
# url = "https://www.aladin.co.kr/shop/usedshop/wc2b_search.aspx?ActionType=1&SearchTarget=Book&KeyWord=9788947547734&x=0&y=0"

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

book = soup.find("table", attrs= {"id" : "searchResult"})
# price = book.find("span", attrs = {"class" : "ss_p2"}).get_text()
# [0:-5]+book.find("span", attrs = {"class" : "ss_p2"}).get_text()[-4:-1])

name = book.find("td", attrs= {"valign" : "top"}).next_sibling.next_sibling.find("strong").get_text()
print(name)
price = book.find("table").next_sibling.next_sibling.find("td", attrs = {"class" : "c2b_tablet3" })
print(price.get_text())
highest = price.next_sibling
print(highest.get_text())
lowest = highest.next_sibling
print(lowest.get_text())
middle = lowest.next_sibling
print(middle.get_text())