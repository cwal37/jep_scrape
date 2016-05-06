# -*- coding: utf-8 -*-
"""
Created on Thu May 05 21:56:45 2016

@author: Connor
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os
import pdb
import nltk


start = time.clock()

# 36x faster to import the csv rather than an xlsx file
df = pd.read_csv('total_scrape_1.csv')
print df.columns

print df.Answers.str.contains('Chicago').sum()

answers = list(df['Answers'])
lc_answers = [w.lower() for w in answers]
df['lc_answers'] = lc_answers

print df.lc_answers.str.contains('chicago').sum()

end = time.clock()
print (end-start)