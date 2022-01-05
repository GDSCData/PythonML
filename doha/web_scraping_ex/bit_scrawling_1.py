import requests
import pandas as pd
from bs4 import BeautifulSoup
from ast import literal_eval
import datetime
from sklearn.ensemble import RandomForestRegressor

today=datetime.date.today().strftime("%Y%m%d")
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                      "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url = 'https://api.finance.naver.com/siseJson.naver?symbol=005930&requestType=1&startTime=20100523&endTime={}&timeframe=day'.format(today)
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')
str1=soup.get_text()
arr=literal_eval(str1)
arr[0].append("내일 값")
for i in range(1,len(arr)-1):
    arr[i].append(arr[i+1][1])
arr[len(arr)-1].append(arr[len(arr)-1][1])
df = pd.DataFrame(arr)
df.to_csv('samsung_data.csv', header=False)
csv = pd.read_csv('samsung_data.csv')
csv_data = csv[['날짜',"시가","고가","저가","종가","거래량","외국인소진율"]]
csv_label = csv["내일 값"]
csv_data2=csv[-1:][['날짜',"시가","고가","저가","종가","거래량","외국인소진율"]]
model1=RandomForestRegressor(n_estimators=200,max_depth=20,max_features='sqrt',min_samples_split=0.001,n_jobs=-1)
model1.fit(csv_data,csv_label)
pre=model1.predict(csv_data2)
print(arr[-1][0],"다음 날 시가 예측:",*pre)