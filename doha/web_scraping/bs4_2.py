# 가우스 전자 웹툰 모든 목차 링크랑 제목 출력

import requests
from bs4 import BeautifulSoup
for i in range(91,0,-1):
    url="https://comic.naver.com/webtoon/list?titleId=675554&page="+str(i)
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'lxml')
    cartoons = soup.find_all("td",attrs={"class":"title"})
    cartoons.reverse()

    for cartoon in cartoons:
        print(cartoon.a.get_text())
        print("https://comic.naver.com"+cartoon.a["href"])
