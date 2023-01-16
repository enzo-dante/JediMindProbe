#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:10:19 2023

@author: enzo_dante
"""

import pandas as pd

FILE_NAME = "articles.xlsx"

COLUMN_ARTICLE_ID = "article_id"
COLUMN_ENGAGEMENT_REACTION_COUNT = "engagement_reaction_count"
COLUMN_ENGAGEMENT_COMMENT_PLUGIN_COUNT = "engagement_comment_plugin_count"
COLUMN_SOURCE_ID = "source_id"
COLUMN_KEYWORD_FLAG = "keyword_flag"
COLUMN_TITLE = "title"

TEST_KEYWORD = "murder"

# read excel or .xlsl file
data = pd.read_excel(FILE_NAME)

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

# dropping column in articles.xlsx
# 'axis=1' refers to dropping a column
data = data.drop(COLUMN_ENGAGEMENT_COMMENT_PLUGIN_COUNT, axis=1)

# get column names in excel file
data.info()

# filter for keyword in article title for new keyword_flag column
def filterForKeyword(keyword):
    
    data_length = len(data)
    keyword_flags = []
    
    for row_index in range(0, data_length):
        
        article_title = data[COLUMN_TITLE][row_index]
        
        # handle null/nan exceptions
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

# create new column in excel dataframe
# transform list into a Series datatype since a Series is 1 column in the dataframe
data[COLUMN_KEYWORD_FLAG] = pd.Series(keyword_occurences)

# sentiment analysis: use NLP to extract approximated opinions of a given text
# VADER: trained ML model on social media dataset that classifies sentiment as either as negative, positive, or neutral
