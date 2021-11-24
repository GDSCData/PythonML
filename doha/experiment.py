import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import GridSearchCV, train_test_split

# MNIST 학습 데이터 읽어 들이기 --- (※1)
csv = pd.read_csv('iris.csv')
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
# csv_data = pd.concat(["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"], axis=1) 이런 방법도 가능,
# 자세한 것은 concat 참고
csv_label = csv["Name"]
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label) # 열 이름에 따라 분류해서 알아서 넣어준다.
print("학습 데이터의 수 =", len(train_label))
# 그리드 서치 매개변수 설정 --- (※3)
params = [
    {"C": [1,10,100,1000], "kernel":["linear"]},
    {"C": [1,10,100,1000], "kernel":["rbf"], "gamma":[0.001, 0.0001]}
]
# 그리드 서치 수행 --- (※4)
clf = GridSearchCV(svm.SVC(), params, n_jobs=-1 )
clf.fit(train_data, train_label)
print("학습기 =", clf.best_estimator_)
# 테스트 데이터 확인하기 --- (※5)
pre = clf.predict(test_data)
ac_score = metrics.accuracy_score(pre, test_label)
print("정답률 =",ac_score)