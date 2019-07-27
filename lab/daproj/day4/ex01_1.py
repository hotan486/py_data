# -*- coding: utf-8 -*-
import pandas as pd


person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')





person_survey1 = pd.merge(survey,person,left_on='person',right_on='ident')
print(person_survey1)

