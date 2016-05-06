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

import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects

plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 13})

def jep_city_word_count():
    start = time.clock()
    
    # 36x faster to import the csv rather than an xlsx file
    jep_df = pd.read_csv('total_scrape_1.csv')
    city_df = pd.read_csv('cities_150.csv')
    
    categories = list(jep_df['Category'])
    lc_cats = [w.lower() for w in categories]
    jep_df['lc_cats'] = lc_cats
    #
    cities = list(city_df['City'])
    lc_cities = [w.lower() for w in cities]
    city_df['lc_cities'] = lc_cities
    
    city_counts = []
    city_counts.append(['City','pop', 'pop_rank', 'Answers', 'Clues', 'Categories'])
    
    i = 1
    for city in list(city_df['City']):
        specific_city_df = city_df[city_df['City'] == city]
        #pdb.set_trace()
        #print city
        #print specific_city_df
        #pdb.set_trace()
        #print specific_city_df['Population']
        pop = specific_city_df['Population']
        pop = pop.values[0]
        answer_count = jep_df.Answers.str.contains(city).sum()
        clue_count = jep_df.Clues.str.contains(city).sum()
        lc_city = city.lower()    
        cat_count = jep_df.lc_cats.str.contains(lc_city).sum()
        city_counts.append([city, pop, i, answer_count, clue_count, cat_count])
        i = i +1
        
    
    city_results = pd.DataFrame(city_counts, columns = city_counts[0])
    city_results.to_csv('city_results.csv')
    
    end = time.clock()
    print (end-start)
    
#jep_city_word_count()


city_results = pd.read_csv('city_results.csv', skiprows=1)

city_results['total_mentions'] = city_results['Answers'] + city_results['Clues']  + city_results['Categories'] 


cres = city_results.sort_values(by = 'total_mentions', ascending=False)

pop10 = city_results[city_results['pop_rank'] <=10]

ind = np.arange(10)
fig, ax1 = plt.subplots()
ax1.bar(ind, pop10['Answers'], color = plt.rcParams['axes.color_cycle'][0], label = 'Answers')
ax1.bar(ind, pop10['Clues'], bottom = pop10['Answers'], color = plt.rcParams['axes.color_cycle'][1], label = 'Clues')
ax1.bar(ind, pop10['Categories'], bottom = pop10['Answers']+pop10['Clues'], color = plt.rcParams['axes.color_cycle'][2], label = 'Categories')


plt.xlabel('Cities')
plt.ylabel('Number of Mentions')
plt.xticks(ind, pop10['City'], rotation=60)
#plt.ylim(0,4000)

ax2 = ax1.twinx()
z = [x+0.5 for x in ind]
ax2.plot(z, pop10['pop']/1000000, label = 'Population', linewidth = 4, color = plt.rcParams['axes.color_cycle'][3])
ax2.set_ylabel('Population in Millions')

ax1.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 5))
ax2.set_yticks(np.linspace(ax2.get_ybound()[0], ax2.get_ybound()[1], 5))
#ax2.set_ylim(0,9.1)

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc=1)


plt.gcf().subplots_adjust(bottom=0.24)

plt.title('Mentions of 10 most Populous US Cities in Jeopardy (1983-2016)')
#plt.show()
plt.savefig('pop10cities.png', dpi=500)





