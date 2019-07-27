# -*- coding: utf-8 -*-
import pandas as pd




pew = pd.read_csv('../data/pew.csv')

#print(pew.shape)
#print(pew.info())
#print(pew.head())


pew_long = pd.melt(pew, id_vars='religion')

print(pew_long)
