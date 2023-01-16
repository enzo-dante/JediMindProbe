#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:10:19 2023

@author: enzo_dante
"""

import pandas as pd
from jedi_mind_probe_strings import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def readData(file):
    
    # read excel or .xlsl file
    data = pd.read_excel(file)
    
    # summary of data
    data.describe()
    
    # summary of the columns
    data.info()
    
    # format of SQL groupby in python:
    # data_frame.groupby(["column_to_group"])["column_to_aggregate"].count()
    
    # count the number of articles per source
    data.groupby([COLUMN_SOURCE_ID])[COLUMN_ARTICLE_ID].count()
    
    # get the total number of reactions by publisher
    data.groupby([COLUMN_SOURCE_ID])[COLUMN_ENGAGEMENT_REACTION_COUNT].sum()
    
    return data

data = readData(FILE_NAME)

def removeColumn(data, column_name):
    
    # dropping column in articles.xlsx
    # 'axis=1' refers to dropping a column
    data = data.drop(column_name, axis=1)
    
    return data

data = removeColumn(data, COLUMN_ENGAGEMENT_COMMENT_PLUGIN_COUNT)

# filter for keyword in article title for new keyword_flag column
def filterForKeyword(keyword):
    
    # get column names in dataframe excel file
    data.info()
    
    data_length = len(data)
    keyword_flags = []
    
    for row_index in range(0, data_length):
        
        article_title = data[COLUMN_TITLE][row_index]
        
        # easier to ask for forgiveness
        # exception handling: if title is null, catch exception
        try:
            if keyword in article_title:
                flag = 1
            else:
                flag = 0               
        except:
            flag = 0
            
        keyword_flags.append(flag)
        
    return keyword_flags

keyword_occurences = filterForKeyword(TEST_KEYWORD)

# create new column in dataframe excel file
# transform list into a Series datatype since a Series is 1 column in the dataframe
data[COLUMN_KEYWORD_FLAG] = pd.Series(keyword_occurences)

# sentiment analysis: use NLP to extract approximated opinions of a given text
def getSentiment(data):
    
    title_negative_sentiments = []
    title_neutral_sentiments = []
    title_positive_sentiments = []
    
    data_length = len(data)
    
    for row_index in range(0, data_length):

        # easier to ask for forgiveness
        # exception handling: if title is null, catch exception        
        try:
            article_title = data[COLUMN_TITLE][row_index]
            
            # VADER: pre-trained ML model on social media dataset that classifies sentiment as % of either negative, positive, & neutral
            # vader compound score: sum of negative, neutral, & positive then normalized(cleaning data with format standardization)
            vader = SentimentIntensityAnalyzer()
            sentiment = vader.polarity_scores(article_title)
            
            neg = sentiment[COLUMN_NEGATIVE]
            neu = sentiment[COLUMN_NEUTRAL]
            pos = sentiment[COLUMN_POSITIVE]
            
        except:
            neg = 0
            neu = 0
            pos = 0
    
        title_negative_sentiments.append(neg)
        title_neutral_sentiments.append(neu)
        title_positive_sentiments.append(pos)
        
    # transform list into a Series datatype since a Series is 1 column in the dataframe
    title_negative_sentiments = pd.Series(title_negative_sentiments)
    title_neutral_sentiments = pd.Series(title_neutral_sentiments)
    title_positive_sentiments = pd.Series(title_positive_sentiments)

    return title_negative_sentiments, title_neutral_sentiments, title_positive_sentiments

# create new columns in dataframe excel file
title_negative_sentiments, title_neutral_sentiments, title_positive_sentiments = getSentiment(data)

data[COLUMN_NEGATIVE_SENTIMENT] = title_negative_sentiments
data[COLUMN_NEUTRAL_SENTIMENT] = title_neutral_sentiments
data[COLUMN_POSITIVE_SENTIMENT] = title_positive_sentiments

# write the normalized data into a new excel file
data.to_excel(CLEAN_FILE_NAME, sheet_name=SHEET_NAME, index=False)
