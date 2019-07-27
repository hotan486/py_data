# -*- coding: utf-8 -*-
import pandas as pd


weather = pd.read_csv('../data/weather.csv')
print(weather.shape)
print(weather.head())
print(weather.tail())



wether_long = pd.melt(
    weather
    ,id_vars=['id','year','month','element']
    ,var_name='day'
    ,value_name='temp'
)

print(wether_long.head(n=10))


# 엑셀 피벗 기능 시도

wether_pivot = wether_long.pivot_table(
    index=['id','year','month','day']
    ,columns='element'
    ,values='temp'
)

print(wether_pivot)


weather_flat = wether_pivot.reset_index()
print(weather_flat)



