from matplotlib.pyplot import plot
from sklearn import svm, metrics, model_selection
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
plot()

csv = pd.read_csv('C:/Users/User/Desktop/git/PythonML/doha/bi/train.csv')
csv2 = pd.read_csv('test.csv')
csv_data = csv[["hour","hour_bef_temperature"]].fillna(-10000)
test_data1 = csv[["hour","hour_bef_temperature"]].fillna(-10000)

csv_label = csv["count"]
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data, csv_label)

best_score = 0

# for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
#     for C in [0.001, 0.01, 0.1, 1, 10, 100]:
#         # 매개변수의 각 조합에 대해 SVC를 훈련시킵니다
#         clf=svm.SVC(gamma=gamma, C=C)
#         clf.fit(train_data, train_label)
#         # 검증 세트로 SVC를 평가합니다
#         score = clf.score(test_data, test_label)
#         # 점수가 더 높으면 매개변수와 함께 기록합니다
#         if score > best_score:
#             best_score = score
#             best_parameters = {'C': C, 'gamma': gamma}
#
#
# # 훈련 세트와 검증 세트를 합쳐 모델을 다시 만든 후
# # 테스트 세트를 사용해 평가합니다
# clf=svm.SVC(**best_parameters)
clf=RandomForestClassifier(n_estimators=100)

# clf = svm.SVC()  # LinearSVC, LinearSVR 등도 있다. RandomForestClassifier 도 있다.
clf.fit(csv_data, csv_label)  # 데이터와 답 넣기
pre = clf.predict(test_data1)

print(pre)
print(pre[0])
cnt=0
fp1=open('submission1.csv', 'w', encoding='utf-8')
with open('submission.csv', 'r', encoding='utf-8') as fp:
    fp=[line.rstrip('\n') for line in fp]
    for i,line in enumerate(fp):
        tmp = line+'\n'
        if i!=0:
            tmp=line+str(pre[cnt])+'\n'
            cnt+=1
        fp1.write(tmp)