# -*- coding: utf-8 -*-
import pandas as pd

# df1 = pd.DataFrame({'id':[1,2,3]},{'age':[11,22,33]})
# df2 = pd.DataFrame({'id':[1,2,3]},{'name':['홍길동','김길동','이길동']})
#
#
# df_merged = pd.merge(df1,df2,on='id')
#
# print(df_merged)

person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')

#print(person)
#print(site)
#print(survey)
#print(visited)


## left_on으로 칼럼으로 잘라서 붙일수 있다
visited_site = pd.merge(visited,site,left_on='site',right_on='name')
print(visited_site)

visited_site = visited_site.drop(columns='name')
print(visited_site)
print("==========================================================")
person_survey = pd.merge(person,survey,left_on='ident',right_on='person')
print(person_survey)



## 오른쪽에 있는 데이텅의 나머지 부분을 확인 할 떄 how를 써 데이터를 볼수 있다

print("==========================================================")
person_survey = pd.merge(person,survey,left_on='ident',right_on='person',how='right')
print(person_survey)

print("==========================================================")
person_survey1 = pd.merge(survey,person,left_on='person',right_on='ident')
print(person_survey1)

person_survey1 = person_survey1.drop(columns='ident')
print(person_survey1)

print("==========================================================")


person_survey1 = pd.merge(person_survey1,survey,left_on='ident',right_on='person',how='right')