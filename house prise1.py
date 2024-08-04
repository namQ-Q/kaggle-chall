import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression




train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

# 숫자형 데이터만 확인해서 예측해보기
train_num = train.select_dtypes(include = ['float64', 'int64'])
train_num.info()
# LotFrontage  TotalBsmtSF  1stFlrSF  GrLivArea  GarageArea  TotRmsAbvGrd
# SalePrice


# 선택한 데이터분포 확인하기(1)
plt.clf()
sns.scatterplot(data = train, x = 'LotFrontage', y = 'SalePrice', s = 3)

# 선택한 데이터 회귀식 확인하기(1)
train[['LotFrontage']].isnull().sum()              # x에 넣을 값에는 nan값이 들어가면 안되니까 확인
Lot_fill = (train[['LotFrontage']].mean() + train[['LotFrontage']].median()) / 2
train[['LotFrontage']] = train[['LotFrontage']].fillna(Lot_fill)

x = train[['LotFrontage']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)
plt.plot(x, pred_y, color='red')                   # 회귀직선 그리기
plt.show()
#                                  ----------> 이 회귀직선으로 예측하면 괜찮을거 같음


# 선택한 데이터분포 확인하기(2)
plt.clf()
sns.scatterplot(data = train, x = 'TotalBsmtSF', y = 'SalePrice', s = 3)

# 선택한 데이터 회귀식 확인하기(2)
train[['TotalBsmtSF']].isnull().sum()

x = train[['TotalBsmtSF']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)
plt.plot(x, pred_y, color='red')                  
plt.show()
#                                  ----------> (1)보다 더 괜찮은거 같음



# 선택한 데이터분포 확인하기(3)
plt.clf()
sns.scatterplot(data = train, x = '1stFlrSF', y = 'SalePrice', s = 3)

# 선택한 데이터 회귀식 확인하기(3)
train[['TotalBsmtSF']].isnull().sum()

x = train[['1stFlrSF']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)
plt.plot(x, pred_y, color='red')                  
plt.show()
#                                  ----------> (1)보다 더 괜찮은거 같음



# 선택한 데이터분포 확인하기(4)
plt.clf()
sns.scatterplot(data = train, x = 'GrLivArea', y = 'SalePrice', s = 3)

# 선택한 데이터 회귀식 확인하기(4)
train[['TotalBsmtSF']].isnull().sum()

x = train[['GrLivArea']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)
plt.plot(x, pred_y, color='red')                  
plt.show()
#                                  ----------> 4개 중에 제일 good



# 선택한 데이터분포 확인하기(5)
plt.clf()
sns.scatterplot(data = train, x = 'GarageArea', y = 'SalePrice', s = 3)

# 선택한 데이터 회귀식 확인하기(5)
train[['GarageArea']].isnull().sum()

x = train[['GarageArea']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)
plt.plot(x, pred_y, color='red')                  
plt.show()
#                                   -----------> 애매하다.



# 선택한 데이터분포 확인하기(6)
plt.clf()
sns.scatterplot(data = train, x = 'TotRmsAbvGrd', y = 'SalePrice', s = 3)

# 선택한 데이터 회귀식 확인하기(6)
train[['TotRmsAbvGrd']].isnull().sum()

x = train[['TotRmsAbvGrd']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)
plt.plot(x, pred_y, color='red')                  
plt.show()
#                                   -----------> 좋지않은것 같다.


# 결론적으로 사용할 데이터는 LotFrontage  TotalBsmtSF  1stFlrSF  GrLivArea  GarageArea
x = train[['LotFrontage', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'GarageArea']]
y = train[['SalePrice']]
model = LinearRegression()
model.fit(x, y)
model.coef_
model.intercept_
pred_y = model.predict(x)              # train데이터의 학습은 끝냈다.

test[['LotFrontage', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'GarageArea']].isnull().sum()
test['LotFrontage'] = test['LotFrontage'].fillna( \
                        (test['LotFrontage'].mean() + test['LotFrontage'].median()) / 2)
test['TotalBsmtSF'] = test['TotalBsmtSF'].fillna( \
                        (test['TotalBsmtSF'].mean() + test['TotalBsmtSF'].median()) / 2)
test['GarageArea'] = test['GarageArea'].fillna( \
                        (test['GarageArea'].mean() + test['GarageArea'].median()) / 2)

test_x = test[['LotFrontage', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'GarageArea']]
pred_y_hat = model.predict(test_x)

sub_df = pd.DataFrame({'Id' : test['Id'],
                       'SalePrice' : test['Id']})
sub_df['SalePrice'] = pred_y_hat
sub_df.to_csv('submission1.csv', index = False)
# 최종점수는 23890,,,,
