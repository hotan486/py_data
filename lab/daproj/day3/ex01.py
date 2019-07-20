# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re
from plotnine import *


pre = pd.read_csv('../data/전국_평균_분양가격_2018.6월_.csv',',',encoding='euc-kr')
print("=============================")
print(pre.head())
print("=============================")
print(pre.tail())

print("클래스 정보=============================")
print(pre.info())

print("=============================")


df2 = pd.DataFrame(data=['대한민국','미국','중국'],
                index=['ko','us','zh'])

print(df2);




print("=============================")


s1 = pd.Series(np.random.rand(5))
print(s1)
print(s1.describe())

print("=============================")

print("=============================")

print("=============================")

print("=============================")

print("=============================")


