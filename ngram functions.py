# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 12:42:27 2019

Contains functions for performing the following:
    1. Generate ngrams from a csv file.
    2. Generate sentences and phrases from a csv file.
    3. Take the output of function #2 and map them to the output of function #1.

@author: USER
"""

import pandas as pd
import os
import functools
import re

# Function using the functools package to concatenate an iterable into one string object.
def reduce_concat(x, sep=""):
    return functools.reduce(lambda x, y: str(x) + sep + str(y), x)


# Function to clean the text from characters and additional white spaces.
def clean_text(str_text):
    return_string =     re.sub(' +', ' ', str_text)
    return_string = re.sub(pattern = "\t|\|",repl = "",string = return_string)
    return_string = re.sub(string = return_string, pattern = "\\'",repl = "'")
    return_string = re.sub(string = return_string, pattern = "\\'",repl = "'")
    return_string = re.sub(string = return_string, pattern = " \? ",repl = "")
    return_string = re.sub(string = return_string, pattern = "\[.*\]",repl = " ")
    return_string = re.sub(string = return_string, pattern = "\<.*\>",repl = " ")
    return_string = re.sub(string = return_string, pattern = " \! ",repl = " ")
    return_string = re.sub(string = return_string, pattern = "\{.*\}",repl = " ")
    return_string = re.sub(string = return_string, pattern = " : ",repl = " ")
    return_string = return_string.lower()
    return(return_string)

#  gen_ngram
# Description: Generate the ngrams for some specific number of spaces, n.
def gen_ngram(str_for_proc,n):
    split_str = [token for token in str_for_proc.split(" ") if token != ""]
    ngrams = zip(*[split_str[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


def unique_count(list_obj):
    bool_vals = [list_txt == unique_results[1] for i in results[0]]


# The function below takes a list of the elements generated by the gen_ngram result.
# It then creates a unique version of the list and counts the number of results for each element
# and places them into a dictionary which is then converted to a pandas data.frame. Finally, the portion of the results.
# that makes up each entry is turned into a percentage.
def count_ngrams(to_check,ngrams_list):
    bool_vals = [list_txt == to_check for list_txt in ngrams_list]
    return(sum(bool_vals))

# Tokenize_Ngram 
# Description: 

# Input:
#   [1] csv file path containing text data. The function will take the values of the csv file, paste them all together.
#       and then tokenize them based on some range of numbers.
# Output: 
#   [1] A dictionary of data frames for each set of ngrams. Each dataframe contains the ngram, its frequency, and its frequency for that specific ngram corpus.
testing = "C:\\Users\\USER\\Dropbox\\Projects\\Adaptive Flash Cards\\Data\\2019-11-24 Testing Data.csv"

def Tokenize_Ngram(csv_file_path):
    s1 = pd.read_csv(csv_file_path,encoding='latin-1')
    s2 = reduce_concat(s1.x,sep = " ")
    s3 = clean_text(s2)
    get_ngrams = gen_ngram(s3,  n=1)
    unique_ngrams = np.unique(get_ngrams)
    result_count = [count_ngrams(word,get_ngrams ) for word in unique_ngrams ]
    count_dict = {unique_ngrams[i]: result_count[i] for i in range(len(unique_ngrams)) }
    ngram_frame =  pd.Series(count_dict).to_frame("Count")    
    ngram_frame["Percent"] = ngram_frame.Count/ngram_frame.Count.sum()
    return(ngram_frame)
 
#hold = Tokenize_Ngram(testing)
# hold2 = pd.Series(hold).to_frame("test")
    
    
    
s2.replace("/\t", "",   regex = True)
s2.replace("|", "")
pd.replace( )




