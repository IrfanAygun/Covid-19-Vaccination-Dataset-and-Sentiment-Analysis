# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:53:06 2021

@author: Fan
"""


import pandas as pd
import numpy as np

### Global ###

input_csv_gb = "gb_dataset.csv"
gb_dataset = pd.read_csv(input_csv_gb)
gb_all = pd.DataFrame(gb_dataset)
gb_all.drop(gb_all.columns[[0,1,2,3,4,5,7,8,9,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33]], axis = 1, inplace = True)
gb_all['user_location'].value_counts()[:100].index.tolist()
gb_count = gb_all['user_location'].value_counts()
#tr_all = tr_all[tr_all.columns[17]]

gb_eng_tweets = gb_all[gb_all["lang"].str.contains("en|english", na=False)]


### United Kingdom ###
UK_tweets = gb_all[gb_all["user_location"].str.contains("UK|England|London|United Kingdom|Ireland|Dublin|Manchester", na=False)]
UK_vaccine_tweets = UK_tweets[UK_tweets["text"].str.contains("vaccine|Astra Zeneca|vaccination|Moderna|Novavax|Sinovac|Pzifer|Biontech|vaxx|Coronavac|Janssen", na=False)]
UK_vaccine_tweets.drop(UK_vaccine_tweets.columns[[1,2,3]], axis = 1, inplace = True)
UK_vaccine_tweets.to_csv(r'UK_vaccinaion_tweets.csv', header=None, index=None, sep=' ', mode='a')

### United Kingdom ###

### USA ###
USA_tweets = gb_all[gb_all["user_location"].str.contains("USA|New York|Washington|Los Angles|Chicago|California|Houston|Florida|Philadephia|Atlanta|Dallas|Las Vegas|Texas|New Jersey|Oregon|Pennsylavania|Alaska|Nevada|Kansas", na=False)]
USA_vaccine_tweets = USA_tweets[USA_tweets["text"].str.contains("vaccine|Astra Zeneca|vaccination|Moderna|Novavax|Sinovac|Pzifer|Biontech|vaxx|Coronavac|Janssen", na=False)]
USA_vaccine_tweets.drop(USA_vaccine_tweets.columns[[1,2,3]], axis = 1, inplace = True)
USA_vaccine_tweets.to_csv(r'USA_vaccinaion_tweets.csv', header=None, index=None, sep=' ', mode='a')

### USA ###

### Canada ###
Canada_tweets = gb_all[gb_all["user_location"].str.contains("Canada|Toronto|Calgary|Vancouver|Montreal|Edmonton|Winnipeg", na=False)]
Canada_vaccine_tweets = Canada_tweets[Canada_tweets["text"].str.contains("vaccine|Astra Zeneca|vaccination|Moderna|Novavax|Sinovac|Pzifer|Biontech|vaxx|Coronavac|Janssen", na=False)]
Canada_vaccine_tweets.drop(Canada_vaccine_tweets.columns[[1,2,3]], axis = 1, inplace = True)
Canada_vaccine_tweets.to_csv(r'Canada_vaccinaion_tweets.csv', header=None, index=None, sep=' ', mode='a')

### Canada ###

### Germany ###
Germany_tweets = gb_all[gb_all["user_location"].str.contains("Deutsc|Germany|Berlin|Deutschland|Hamburg|Munich|Munchen|Frankfurt|Dortmund|Cologne|Köln|Stuttgart|Bremen", na=False)]
Germany_vaccine_tweets = Germany_tweets[Germany_tweets["text"].str.contains("vaccine|Astra Zeneca|vaccination|Moderna|Novavax|Sinovac|Pzifer|Biontech|vaxx|Coronavac|Janssen", na=False)]
Germany_vaccine_tweets.drop(Germany_vaccine_tweets.columns[[1,2,3]], axis = 1, inplace = True)
Germany_vaccine_tweets.to_csv(r'Germany_vaccinaion_tweets.csv', header=None, index=None, sep=' ', mode='a')

### Canada ###

### France ###
France_tweets = gb_all[gb_all["user_location"].str.contains("France|Paris|Lyon|Marseille|Tolouse|Nice|Lille|Reims|Rennes|Nantes|Strasbourg", na=False)]
France_vaccine_tweets = France_tweets[France_tweets["text"].str.contains("vaccine|Astra Zeneca|vaccination|Moderna|Novavax|Sinovac|Pzifer|Biontech|vaxx|Coronavac|Janssen", na=False)]
France_vaccine_tweets.drop(France_vaccine_tweets.columns[[1,2,3]], axis = 1, inplace = True)
France_vaccine_tweets.to_csv(r'France_vaccinaion_tweets.csv', header=None, index=None, sep=' ', mode='a')

### France ###

### Spain ###
Spain_tweets = gb_all[gb_all["user_location"].str.contains("Spain|Espana|España|Madrid|Barcelona|Valencia|Seville|Bilbap|Malaga|Sagunto|Gijon", na=False)]
Spain_vaccine_tweets = Spain_tweets[Spain_tweets["text"].str.contains("vaccine|Astra Zeneca|vaccination|Moderna|Novavax|Sinovac|Pzifer|Biontech|vaxx|Coronavac|Janssen", na=False)]
Spain_vaccine_tweets.drop(Spain_vaccine_tweets.columns[[1,2,3]], axis = 1, inplace = True)
Spain_vaccine_tweets.to_csv(r'Spain_vaccinaion_tweets.csv', header=None, index=None, sep=' ', mode='a')

### France ###

### Italy ###
Italy_tweets = gb_all[gb_all["user_location"].str.contains("Italy|Rome|Milano|Milan|Naples|Turin|Torino|Palermo|Genoa|Bologna|Florence|italiano|Italiano", na=False)]
Italy_vaccine_tweets = Italy_tweets[Italy_tweets["text"].str.contains("vaccine|Astra Zeneca|vaccination|Moderna|Novavax|Sinovac|Pzifer|Biontech|vaxx|Coronavac|Janssen", na=False)]
Italy_vaccine_tweets.drop(Italy_vaccine_tweets.columns[[1,2,3]], axis = 1, inplace = True)
Italy_vaccine_tweets.to_csv(r'Italy_vaccinaion_tweets.csv', header=None, index=None, sep=' ', mode='a')

### Italy ###

### Türkiye ###
tr_df = dataset[dataset['tweet_content'].str.contains('tr', na=False)]
tr_df_id = tr_df['tweet_content'].str[:19]
tr_df_id.to_csv(r'tr_dataset.txt', header=None, index=None, sep=' ', mode='a')

input_csv = "tr_dataset.csv"
tr_dataset = pd.read_csv(input_csv)
tr_all = pd.DataFrame(tr_dataset)
tr_all.drop(tr_all.columns[[0,1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]], axis = 1, inplace = True)
#tr_all = tr_all[tr_all.columns[17]]

tr_tweets = tr_all[tr_all["text"].str.contains("aşı|sinovac|pzifer|biontech|astrazeneca|moderna|novavax", na=False)]
del tr_tweets['text']

tr_tweets.to_csv(r'dataset_turkey.csv', header=None, index=None, sep=' ', mode='a')

### Türkiye ###