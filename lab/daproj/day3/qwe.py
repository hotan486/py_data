## numpy

import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt2

df = pd.read_csv('../data/gapminder.tsv', sep='\t')
print(type(df))
##
print(df.head(n=3))
##
print(df.tail(n=5))

## 열과 행의 갯수
print(df.shape)

## 칼럼
print(df.columns)


## 각 칼럼 값 확인하기
for col in df.columns:
    print(col)

##칼럼의 타입 저장 확인하기
print(df.dtypes)

print('================================')
## 요약 정보
df.info()


##
countries = df['country']
print(countries)
print(type(countries))
# Series 1차원 배열
# DataFrame 2차원 배열

print('================================')
subset = df[['country' , 'year' , 'lifeExp']]
print(type(subset))
print('================================')
subset.info()
print('================================')
print(subset.head(n=5))
print('================================')
print(df.loc[0])
print('================================')
print(df.iloc[0])
print('================================')
print(type(df.loc[0]))
print('================================')
subset2 = df.loc[[0,10,20]]
print(subset2)
print('================================')
print(df.loc[840:851])
print('================================')
kor1 = df.loc[840:851,['country' , 'year' , 'lifeExp']]
print(kor1)
print('================================')
kor2 = df.iloc[840:852,[0,2,3]]
print(kor2)
## loc 칼럼값 사용 iloc 인덱스 사용
print('================================')
# 연도별 lifeExp의 평균
print(df.groupby('year')['lifeExp'].mean())
print('================================')
year_group = df.groupby('year')
print(type(year_group))
print('================================')
print(year_group)
print('================================')
year_group_lifeExp = year_group['lifeExp']
print(type(year_group_lifeExp))
print(year_group_lifeExp)
print('================================')
mean = year_group_lifeExp.mean()
print(mean)
print('================================')
# 연도별 lifeExp의 평균
print(df.groupby('year')['pop'].sum())
print('================================')
print(df['year'] > 1980)
print('================================')
print(df[df['year'] > 1980])
print('================================')
print(df[df['year'] > 2000][['country','pop']])
print('================================')
print(df[df['country'] == 'Korea, Rep. '])

# print('================================')
# print(df[df['country'].str.contains('Korea')])
# print('=========================================')
# print('대륙별 평균 수명 ==========================')
# print(df.groupby('continent')['lifeExp'].mean())
# print('=========================================')

# print('=========================================')
# print('대륙별 년도별 평균 수명 ====================')
# print(df.groupby(['continent', 'year'])['lifeExp'].mean())
# print('=========================================')
