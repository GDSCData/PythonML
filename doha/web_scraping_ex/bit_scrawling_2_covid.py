import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
from sklearn.ensemble import RandomForestRegressor

today = datetime.date.today().strftime("%Y%m%d")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url_kr = 'https://coronaboard.kr/generated/KR.json'

res = requests.get(url_kr)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
KR_dict = json.loads(soup.get_text())
KR_pd = pd.DataFrame(KR_dict)
#KR_pd.index = pd.to_datetime(KR_pd["date"], format='%Y%m%d')
KR_pd = KR_pd.drop(columns='date')
KR_data = KR_pd.iloc[:, 5:6]
print(KR_data.loc[len(KR_data.index)-1])
if KR_data.loc[len(KR_data.index)-1]['confirmed']!=0:
    KR_data.loc[len(KR_data.index)] =0
    KR_pd.loc[len(KR_pd.index)] =0
KR_data["-1"]=KR_pd.iloc[:, 5:6].shift(periods=1, fill_value=0)
KR_data["-2"]=KR_pd.iloc[:, 5:6].shift(periods=2, fill_value=0)
KR_data["-3"]=KR_pd.iloc[:, 5:6].shift(periods=3, fill_value=0)
KR_data["-4"]=KR_pd.iloc[:, 5:6].shift(periods=4, fill_value=0)
KR_data["-5"]=KR_pd.iloc[:, 5:6].shift(periods=5, fill_value=0)
KR_data["-6"]=KR_pd.iloc[:, 5:6].shift(periods=6, fill_value=0)
KR_data["-7"]=KR_pd.iloc[:, 5:6].shift(periods=7, fill_value=0)
KR_data["-8"]=KR_pd.iloc[:, 5:6].shift(periods=8, fill_value=0)
KR_test=KR_data.tail(1)
print(KR_data)
KR_data.drop(KR_data.tail(1).index,inplace=True)
X=KR_data[["-1","-2","-3","-4","-5","-6","-7","-8"]]
y = KR_data['confirmed']
model1=RandomForestRegressor(n_estimators=1000,max_depth=20,max_features='sqrt',min_samples_split=0.0005,n_jobs=-1)
model1.fit(X,y)
pre=model1.predict(KR_test[-1:][["-1","-2","-3","-4","-5","-6","-7","-8"]])
print(pre)
