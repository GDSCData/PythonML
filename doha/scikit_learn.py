from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

# 기본 scikit-learn
xor_input = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
xor_df = pd.DataFrame(xor_input)
data = xor_df.loc[:, 0:1]  # 전 구간, 0부터 1번 index 값이 데이터
label = xor_df.loc[:, 2]  # 전 구간, 2번 index 값이 데이터
data1 = [True, False]
clf = svm.SVC()
clf.fit(data, label)  # 데이터와 답 넣기
pre = clf.predict(data1)  # data1으로 예측값 도출하기
ac_score = metrics.accuracy_score(label, pre)  # 실제 답과 예측결과를 넣어서 바로 퍼센티지를 구해준다.
cl_report = metrics.classification_report(label, pre)  # 리포트 결과 확인도 가능
# pandas 를 이용한 scikit-learn
csv = pd.read_csv('iris.csv')
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)
# 열 이름에 따라 분류해서 알아서 넣어준다.
