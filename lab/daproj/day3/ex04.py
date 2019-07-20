# -*- coding: utf-8 -*-
from unittest.mock import inplace

import pandas as pd

print('========================================')

df1 = pd.read_csv('../data/concat_1.csv')


print(df1)
print('========================================')

df2 = pd.read_csv('../data/concat_2.csv')


print(df2)
print('========================================')


df3 = pd.read_csv('../data/concat_3.csv')


print(df3)
print('합치기========================================')

row_concat = pd.concat([df1,df2,df3])
print(row_concat)
print('========================================')
print(row_concat.loc[0])
print(row_concat.iloc[0])
print(row_concat.reset_index(inplace=False))
print(row_concat.reset_index(inplace=True))
dropped = row_concat.drop('index',axis=1)
print(dropped)