import imp
import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title.get_text())
# print(soup.a)
 
# print(soup.find("a", attrs = {"class" : "Nbtn_upload"}))
# print(soup.find(attrs = {"class" : "Nbtn_upload"}))
rank1 = soup.find("li", attrs = {"class" : "rank01"} )
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())

webtoon = soup.find("a", text = "먹는 인생-21화 치킨")
print(webtoon)