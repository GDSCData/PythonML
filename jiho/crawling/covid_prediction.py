from ast import literal_eval
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split

# 거리두기 turning point 날짜 별로 거리두기 저장
def distancetp_to_datetime(all_dates, tp_dates):
    dist_info_list = list()
    tp = list([datetime.strptime(date, "%Y-%m-%d") for date in tp_dates])

    for date in all_dates:
        comp_date = datetime.strptime(date, "%Y-%m-%d")

        if comp_date <= tp[0]:
            dist_info_list.append(0)
        elif comp_date <= tp[1]:
            dist_info_list.append(1)
        elif comp_date <= tp[2]:
            dist_info_list.append(1.5)
        elif comp_date <= tp[3]:
            dist_info_list.append(2.5)
        elif comp_date <= tp[4]:
            dist_info_list.append(1)
        elif comp_date <= tp[5]:
            dist_info_list.append(2)
        elif comp_date <= tp[6]:
            dist_info_list.append(4)
        elif comp_date <= tp[7]:
            dist_info_list.append(4.3)
        elif comp_date <= tp[8]:
            dist_info_list.append(4)
        elif comp_date <= tp[9]:
            dist_info_list.append(4.5)
        else:
            dist_info_list.append(4.4)

    return dist_info_list


# list acc
def calculate_array_acc(array):
    result_array = list()
    acc = 0

    for a in array:
        acc = acc + a
        result_array.append(acc)

    return result_array


# DataFrame 열 위치 변경
def change_col(df, col1, col2):
    return df[[col1 if c == col2 else col2 if c == col1 else c for c in df.columns]]


"""

받아온 데이터 columns

date
active
confirmed_acc
death_acc
released_acc
critical_acc
confirmed
death
released
critical

"""

res = requests.get("https://coronaboard.kr/generated/KR.json")
soup = BeautifulSoup(res.content, "html.parser")

covid_dict = json.loads(soup.text)

""" Update date string format : 20210227 -> 2021-02-27 """
for idx, date in enumerate(covid_dict["date"]):
    covid_dict["date"][idx] = "{year}-{mon}-{day}".format(
        year=date[:4], mon=date[4:6], day=date[6:]
    )

""" 백신 접종 현황 """
vaccine_res = requests.get(
    "https://apiv3.corona-live.com/vaccine/ts/first-and-second/all.json?timestamp=1642231265956"
)
vaccine_soup = BeautifulSoup(vaccine_res.content, "html.parser")

vaccine_dict = literal_eval(vaccine_soup.text)

vaccine_first = list()
vaccine_second = list()
vaccine_booster = list()

for idx, date in enumerate(covid_dict["date"]):
    if idx < len(covid_dict["date"]) - len(vaccine_dict["first"]):
        vaccine_first.append(0)
        vaccine_second.append(0)
        vaccine_booster.append(0)
    else:
        vaccine_first.append(vaccine_dict["first"][date])
        vaccine_second.append(vaccine_dict["second"][date])
        vaccine_booster.append(vaccine_dict["booster"][date])

vaccine_first_acc = calculate_array_acc(vaccine_first)
vaccine_second_acc = calculate_array_acc(vaccine_second)
vaccine_booster_acc = calculate_array_acc(vaccine_booster)

""" 거리두기 현황 데이터 """
distance_tp_list = [
    "2020-03-23",
    "2020-11-16",
    "2020-11-30",
    "2021-01-31",
    "2021-02-14",
    "2021-07-11",
    "2021-07-26",
    "2021-10-31",
    "2021-12-17",
    "2022-01-16",
]
dist_info_list = distancetp_to_datetime(covid_dict["date"], distance_tp_list)

""" 
Merge the following additional column data into covid_dict

vaccine_first 
vaccine_second
vaccine_booster
vaccine_first_acc
vaccine_second_acc
vaccine_booster_acc
dist_info_list

"""
covid_dict["vaccine_first"] = vaccine_first
covid_dict["vaccine_second"] = vaccine_second
covid_dict["vaccine_booster"] = vaccine_booster
covid_dict["vaccine_first_acc"] = vaccine_first_acc
covid_dict["vaccine_second_acc"] = vaccine_second_acc
covid_dict["vaccine_booster_acc"] = vaccine_booster_acc
covid_dict["dist_info_list"] = dist_info_list

""" From Dict To DataFrame """
covid_df = pd.DataFrame.from_dict(covid_dict, orient="index").transpose()
covid_df.set_index("date", inplace=True)  # date 를 index로 설정
covid_df.index = pd.to_datetime(covid_df.index)  # DataFrame의 index를 연속된 날짜로 변경
covid_df = change_col(
    covid_df, "active", "confirmed"
)  # DataFrame "active", "confirmed" 열 위치 변경
covid_df = covid_df.fillna(0)

label = []
data = []
attr_list = []

for row_index, row in covid_df.iterrows():
    label.append(row[0])
    row_data = []
    for v in row[1:]:
        row_data.append(v)
    data.append(row_data)

predict_data = [data[-1]]
predict_label = label[-1]
data.pop()
label.pop()

""" 학습 전용과 테스트 전용 데이터로 나누기 """
data_train, data_test, label_train, label_test = train_test_split(data, label)

""" 모델 생성 """
clf = RandomForestRegressor()

""" 모델 학습 """
clf.fit(data_train, label_train)

""" 모델 검증 """
print("===== 모델 검증 =====")
print("Train: ", clf.score(data_train, label_train))
print("Test: ", clf.score(data_test, label_test))

""" 모델 예측 """
print("\n===== 모델 예측 =====")
predict_result = clf.predict(predict_data)
print(f"금일 코로나 확진자 : {predict_label}")
print(f"예측 모델 : {predict_result[0]}")
