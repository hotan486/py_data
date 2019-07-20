# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re
from plotnine import *

df = pd.read_csv('../data/전국_평균_분양가격_2018.6월_.csv',',',encoding='euc-kr')

print('=======================================')
print(df)
print('=======================================')
print(df.info())
print('=======================================')
print(df.shape)
print('=======================================')
cols = ['지역명','연도','월','분양가격(㎡)']
print(df[cols])
print('=======================================')
print(df.describe(include='all'))
print('=======================================')
#print(df['분양가격(㎡)'].mean())