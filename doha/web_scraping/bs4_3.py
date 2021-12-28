# 쿠팡에서 노트북이라는 키워드로 검색해서 1~4페이지까지 출력

import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
for i in range(1,5):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid" \
          "=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false" \
          "&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor= ".format(i)
    res=requests.get(url,headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")

    lists=soup.find_all("li",attrs={"class":"search-product"})
    for list in lists:
        print(i,":",list.find("div",attrs={"class":"name"}).get_text())

# 이미지 가져오는 방법: https://www.youtube.com/watch?v=yQ20jZwDjTE&t=9889s 가서 18번 목차 듣기.
