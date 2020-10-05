 -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:55:58 2020
@author: Anustup
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

df = pd.read_csv(r"C:\Users\Anustup\Desktop\users.csv")

features = ['Name','Keywords','Job_Role','Location']

for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['Name'] +" "+row['Keywords']+" "+row["Job_Role"]+" "+row["Location"]
	except:
		print( "Error:", row	)

df["combined_features"] = df.apply(combine_features,axis=1)

cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(count_matrix) 
Similar_profile = "Anustup"

## Step 6: Get index of this movie from its title
User_index = get_index_from_title(Similar_profile)

similar_users =  list(enumerate(cosine_sim[User_index]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_users = sorted(similar_users,key=lambda x:x[1],reverse=True)

## Step 8: Print titles of first similar profiles
i=0
print("Top 5 similar profiles to "+Similar_profile+" are:\n")
for element in sorted_similar_users:
		print (get_title_from_index(element[0]))
		i=i+1
		if i>5:
			break
