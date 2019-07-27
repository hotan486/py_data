# -*- coding: utf-8 -*-
import pandas as pd




pew = pd.read_csv('../data/pew.csv')

#print(pew.shape)
#print(pew.info())
#print(pew.head())

# 파라미터 만들기
# 멜트 =
pew_long = pd.melt(pew, id_vars='religion')
print(pew_long.head(n=10))
# 이름 지정
pew_long = pd.melt(pew,
                   id_vars='religion'
                   ,var_name='income'
                   , value_name='갯수')
print(pew_long.head(n=10))

# 종교 출력
print(pew_long['religion'].unique())

# 소득 단위
print(pew_long['income'].unique())




# 소득 >150k 인 데이터만 추출 -> 내림 정렬
income_max = pew_long[pew_long['income'] == '>150k'].sort_values(by='갯수',ascending=False)
print(income_max)

income_max = pew_long[pew_long['income'] == '>150k'].sort_values(by='갯수',ascending=False)
print(income_max)




