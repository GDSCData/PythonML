import numpy
import requests
import pandas as pd
from bs4 import BeautifulSoup
from ast import literal_eval

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = 'https://api.finance.naver.com/siseJson.naver?symbol=005930&requestType=1&startTime=20100523&endTime=20210101&timeframe=day'
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')
str=soup.get_text()
arr=literal_eval(str)
print(arr)

df = pd.DataFrame(arr)
df.to_csv('samsung_data.csv', header=False)