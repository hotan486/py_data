# -*- coding: utf-8 -*-
import pandas as pd

user_cols = ['user_id','gender','age','occupation','zip']
users = pd.read_csv('../data/movielens/users.dat',sep='::',header=None,names=user_cols,engine='python');
#print(user)
rating_cols=['user_id','movie_id','rating','timestamp']
ratings = pd.read_csv('../data/movielens/ratings.dat',sep='::',header=None,names=rating_cols,engine='python')
#print(ratings)

movie_cols = ['movie_id','title','generes']
movies=pd.read_csv('../data/movielens/movies.dat',sep='::',header=None,names=movie_cols,engine='python')
#print(movies.head())


# 겹치는 칼럽이 있으면 on 생략 가능
#data=pd.merge(ratings, users)
#data=pd.merge(data, movies)
data=pd.merge(pd.merge(ratings, users), movies)

#print(data.head())


m = data.pivot_table(
    'rating',
    index='title'
    ,columns='gender'
    ,aggfunc='mean'
)
#print(m[:5])

ti = data.groupby('title').size()
#print(ti)


sds = ti.index[ti >= 300]
#print(sds)


q1 = m.loc[sds]
print(q1[:5])


top = m.sort_values(by='F',ascending=False)
top = m.sort_values(by='M',ascending=False)
m['diff'] = m['M'] - m['F']
print(m[:5])
asd1 = m.sort_values(by='diff')
print(asd1[:10])