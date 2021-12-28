# 네이버 웹툰 모든 제목 가져와보기

import requests
from bs4 import BeautifulSoup
url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')
print(soup.title.get_text())
print(soup.a)  # 첫번째로 발견되는 a 가져오기
print(soup.a.attrs)  # 첫번째로 발견되는 a dict 형태로 안에꺼 가져오기
rank1=soup.find("li",attrs={"class":"rank01"})  # 해당 li 가져오기
rank2=rank1.next_sibling.next_sibling  # 다음 형제 가져오기. parent, previous 도 가능
rank3=rank1.find_next_sibling("li")  # 자동으로 다음 li만 가져옴. 개행 span 무시 가능 siblings 도 가능
print(rank2.a.get_text())

cartoons=soup.find_all("a",attrs={"class": "title"})  # 제목만 다 가져오기
for cartoon in cartoons:
    print(cartoon.get_text())
