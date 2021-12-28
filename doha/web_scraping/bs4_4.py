# 네이버 증권 거래량 순으로 200등까지 받아와서 csv 에 저장하기.

import requests
from bs4 import BeautifulSoup
import re
import csv

filename="시가총액.csv"
f=open(filename,"w",encoding="utf8",newline="")
writer=csv.writer(f)
p=re.compile("^[^토].*")  # 토로 시작하지 않는 모든 것. 토론장 이라는 것만 빼고 다 가져오기 위해서 만듦
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
for i in range(1,5):

    res=requests.get(url+str(i),headers=headers)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    head = soup.find("table", attrs={"class": "type_2"}).find("thead").find_all("th",text=p)
    head_data = [name.get_text().strip() for name in head]
    writer.writerow(head_data)

    data_row=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr",attrs={"onmouseover":p})
    for row in data_row:
        columns=row.find_all("td")
        data = [column.get_text().strip() for column in columns]
        print(data)
        writer.writerow(data)
