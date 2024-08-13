import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# house price1에서 사용한 변수에서 이상치를 제거하고 돌려보자!

# 선택한 데이터 회귀식 확인하기(1)
train[['LotFrontage']].isnull().sum()
Lot_fill = (train[['LotFrontage']].mean() + train[['LotFrontage']].median()) / 2
train[['LotFrontage']] = train[['LotFrontage']].fillna(Lot_fill)

plt.clf()
sns.scatterplot(data = train, x = 'LotFrontage', y = 'SalePrice', s = 3)
# scatter에 이상치 2개 발견
train['LotFrontage'].sort_values(ascending = False).head()
train['LotFrontage'] = train['LotFrontage'].drop([1298, 934])
sns.scatterplot(data = train, x = 'LotFrontage', y = 'SalePrice', s = 3)
x = train[['LotFrontage']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)
plt.plot(x, pred_y, color='red')                   # 회귀직선 그리기
plt.show()







