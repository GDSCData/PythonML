# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from sklearn import svm

# XOR의 계산 결과 데이터
xor_data = [
    # P, Q, Result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 1, 0]
]

# 학습을 위해 데이터와 레이블 분리하기 -> fit() 메서드의 매개변수를 맞추기 위함
data = [] # 학습시키기 위한 데이터 변수
label = [] # 정답 레이블 변수
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

# 데이터 학습시키기
clf = svm.SVC() # SVM 객체 생성
# fit() 메서드를 사용해 데이터를 학습시킴
clf.fit(data, label) # fit(첫 번째 매개변수로 학습할 데이터 배열, 두 번째 매개변수로 정답 레이블 배열)

# 데이터 예측하기
pre = clf.predict(data) # 예측하고 싶은 데이터 배열을 전달하면 데이터 수만큼 예측 결과를 리턴
print(" 예측결과:", pre)

# 결과 확인하기
ok = 0; total = 0
for index, answer in enumerate(label):
    p = pre[index]
    if p == answer: ok += 1
    total += 1
print("정답률:", ok, "/", total, "=", ok/total)
# -

# ## 프레임워크로 프로그램 간단하게 작성
# scikit-learn 에는 데이터와 레이블을 나누고, 정답률을 간단하게 계산해주는 기능이 존재

# +
import pandas as pd
from sklearn import svm, metrics

# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 1, 0]
]

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.loc[:,0:1] # 데이터
xor_label = xor_df.loc[:,2] # 레이블

# 데이터 학습과 예측하기
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 = ", ac_score)
# -

# ### Pandas loc() 로 열 조회하기
# - 모든 행은 : 로 표시하고 쉼표(,)를 입력하고 열명을 입력하면 해당 열만 가져온다.

# +
import pandas as pd

data = [
    [100, 25, 10],
    [200, 20, 11],
    [300, 15, 12],
    [350, 16, 13],
    [320, 17, 12]
]

df = pd.DataFrame(data, 
                  index=['1월', '2월', '3월', '4월', '5월'], 
                  columns=['매출액', '영업이익', '순이익'])
# display(df) # 예쁘게 보여줌ㅋ

# 열 조회하기

df.loc[:, '매출액'] # 배열 형태가 아닌 값을 입력하면 1차원 시리즈 형태가 리턴된다.
df.loc[:, ['매출액']] # 배열 형태로 열명을 입력 시 2차원 데이터프레임 형태가 리턴
df.loc[:, df.columns != '매출액'] # 특정 열만 제외한 나머지 열을 리턴
df.loc[:, '매출액':'순이익'] # 인덱싱으로 매출액 열에서 순이익 열까지의 열 값들을 가져올 수 있다.
df.loc[:, [False, True, True]] # 열 개수와 동일한 True/False의 배열을 지정해 True인 열만 가져올 수 있다.
# -


















