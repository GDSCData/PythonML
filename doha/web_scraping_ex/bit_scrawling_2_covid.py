import json
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
from bs4 import BeautifulSoup
from ast import literal_eval
import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

today = datetime.date.today().strftime("%Y%m%d")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                         "537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
url_us = 'https://coronaboard.kr/generated/KR.json'
url_kr = 'https://coronaboard.kr/generated/KR.json'
url_jp = 'https://coronaboard.kr/generated/JP.json'
url_CN = 'https://coronaboard.kr/generated/CN.json'
url_CA = 'https://coronaboard.kr/generated/CA.json'
url_DE = 'https://coronaboard.kr/generated/DE.json'
res = requests.get(url_us)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
US_dict = json.loads(soup.get_text())
US_pd = pd.DataFrame(US_dict)
US_pd.index = pd.to_datetime(US_pd["date"], format='%Y%m%d')
US_pd = US_pd.drop(columns='date')
print(US_dict.keys())
print(US_pd.head(5))
US_pd["critical"] = US_pd["critical"].fillna(0)
US_pd["critical_acc"] = US_pd["critical_acc"].fillna(0)
X = US_pd
y = US_pd.iloc[:, 5:6]
print(X.tail(5))
print(y)
# 'date', 'active', 'confirmed_acc', 'death_acc', 'released_acc', 'critical_acc', 'confirmed', 'death', 'released'
# 날짜, 치료 중, 확진자 누적, 사망자 누적, 완치자 누적, ?, 확진자 일별, 사망자 일별, 완치자 일별

