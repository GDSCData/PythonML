import requests
from bs4 import BeautifulSoup
import traceback
import pandas as pd
from pandas import DataFrame
import datetime
import os

code = "000660"
url = "https://finance.naver.com/item/sise_day.naver?code={code}".format(code=code)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

el_table_navi = soup.find("table", class_="Nnavi")
el_td_last = el_table_navi.find("td", class_="pgRR")
pg_last = el_td_last.a.get('href').rsplit('&')[1]
pg_last = pg_last.split('=')[1]
pg_last = int(pg_last)


def parse_page(code, page):
    site = "http://finance.naver.com/item/sise_day.naver?code={code}&page={page}".format(code=code, page=page)
    re = requests.get(site, headers=headers)
    _soap = BeautifulSoup(re.text, 'lxml')
    html_table = _soap.select("table")
    _df = pd.read_html(str(html_table))
    df_day = _df[0].dropna()
    return df_day


date_start = datetime.datetime.strftime(datetime.datetime(year=2018, month=1, day=1), '%Y.%m.%d')
date_end = datetime.datetime.strftime(datetime.datetime.today(), '%Y.%m.%d')

df = None
for page in range(1, pg_last+1):
    _df = parse_page(code, page)
    _df_filtered = _df[_df['날짜'] > date_start]
    if df is None:
        df = _df_filtered
    else:
        df = pd.concat([df, _df_filtered])
    if len(_df) > len(_df_filtered):
        break

path_dir = 'data/2022-01-03-crawling'
if not os.path.exists(path_dir):
    os.makedirs(path_dir)
path = os.path.join(path_dir, '{code}_{date_from}_{date_to}.csv'.format(code=code, date_from=date_start, date_to=date_end))

df.to_csv(path, index=False)