import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns
train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')
submission=pd.read_csv('submission.csv')

print(train.groupby('hour').mean()['count'])
plt.plot(train.groupby('hour').mean()['count'],'o-')
plt.grid()
plt.title('count by hours', fontsize=15)
plt.savefig('pic.png')

plt.figure(figsize=(10,10))
sns.heatmap(train.corr(),annot=True)
print(train.isna().sum())
print(train.groupby('hour').mean()['hour_bef_humidity'])
#print(train[test['hour_bef_humidity'].isna()])
test['hour_bef_humidity'].fillna(43.573770 ,inplace=True)

features=['hour','hour_bef_temperature','hour_bef_windspeed','hour_bef_ozone','hour_bef_humidity']
X_train=train[features]
Y_train=train['count']
X_test=test[features]

model100=RandomForestRegressor(n_estimators=100,random_state=0,n_jobs=-1)
model100_5=RandomForestRegressor(n_estimators=100,max_depth=5,random_state=0,n_jobs=-1)
model200=RandomForestRegressor(n_estimators=1000,n_jobs=-1)

model100.fit(X_train,Y_train)
model100_5.fit(X_train,Y_train)
model200.fit(X_train,Y_train)

pre1=model100.predict(X_test)
pre2=model100_5.predict(X_test)
pre3=model200.predict(X_test)

submission['count']=pre3
submission.to_csv('model200.csv',index=False)