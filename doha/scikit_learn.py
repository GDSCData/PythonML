from sklearn import svm, metrics, model_selection
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

# 기본 scikit-learn
xor_input = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
xor_df = pd.DataFrame(xor_input)
data = xor_df.loc[:, 0:1]  # 전 구간, 0부터 1번 index 값이 데이터
label = xor_df.loc[:, 2]  # 전 구간, 2번 index 값이 데이터
data1 = [True, False]
clf = svm.SVC()  # LinearSVC, LinearSVR 등도 있다. RandomForestClassifier(n_jobs=-1 로 최대속도, max_depth 도 수정) 도 있다.
clf.fit(data, label)  # 데이터와 답 넣기
joblib.dump(clf, "freq.pkl")  # 파일로 데이터 저장하기
pre = clf.predict(data1)  # data1으로 예측값 도출하기
ac_score = metrics.accuracy_score(label, pre)  # 실제 답과 예측결과를 넣어서 바로 퍼센티지를 구해준다.
cl_report = metrics.classification_report(label, pre)  # 리포트 결과 확인도 가능

# pandas 를 이용한 scikit-learn
csv = pd.read_csv('iris.csv')
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
# csv_data = pd.concat(["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"], axis=1) 이런 방법도 가능,
# 자세한 것은 concat 참고
csv_label = csv["Name"]
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label) # 열 이름에 따라 분류해서 알아서 넣어준다.

scores = model_selection.cross_val_score(clf, data, label, cv=5)  # 크로스 validation, 테스트 데이터와
# train 데이터를 5등분 해가지고, 총 5번 다르게 설정해서 구한다. 같은 것을 5번 반복.

label = []
data = []
attr_list = []
for row_index, row in csv.iterrows():
    label.append(row.loc[0])
    row_data = []
    for v in row.loc[1:]:
        row_data.append(ord(v))
    data.append(row_data)  # 이런식으로 열 이름이 없어도 분류가 가능하다. 여기서는 각 문자에 대응하는 숫자로 dataset 을 만들어 주었다.
# 이 때 일어날 수도 있는 문제점이, 만약 숫자가 빨강=1, 파랑=2 라면 파랑이 빨강의 2배라는 오해를 프로그램이 할 수도 있기 때문에
# 안전하게 빨강 = [1,0], 파랑=[0,1] 등으로 하는 것이 좋다. 아래는 그렇게 코드를 바꾼 것이다.
for row_index, row in csv.iterrows():
    label.append(row.loc[0])
    exdata = []
    for col, v in enumerate(row.loc[1:]):
        if row_index == 0:
            attr = {"dic": {}, "cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        # 버섯의 특징 기호를 배열로 나타내기
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)
# 시각화 하기 위한 matplotlib 은 알아서 찾아보자! 일부로 안적었다. 잘 안쓰일 것 같아서

# 그리드 서치는, 매개변수로 어떤 것이 좋을지 자동으로 판별해주는 문법이다! 책에는 제대로 안나와서 다시 찾아보자!
