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
from nltk.corpus import stopwords

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
        cat_count = jep_df.lc_cats.str.contains(lc_city).sum()/5
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
    pop10 = cres[0:10]
    #pop10 = city_results[city_results['pop_rank'] <=10]
    
    ind = np.arange(10)
    fig, ax1 = plt.subplots()
    ax1.bar(ind, pop10['Answers'], color = plt.rcParams['axes.color_cycle'][0], label = 'Answers')
    ax1.bar(ind, pop10['Clues'], bottom = pop10['Answers'], color = plt.rcParams['axes.color_cycle'][1], label = 'Clues')
    ax1.bar(ind, pop10['Categories'], bottom = pop10['Answers']+pop10['Clues'], color = plt.rcParams['axes.color_cycle'][2], label = 'Categories')
    
    
    plt.xlabel('Cities')
    plt.ylabel('Number of Mentions')
    cities = list(pop10['City'])
    cities = [str(x) for x in cities]
    y = [x+0.25 for x in ind]
    plt.xticks(y, cities, rotation=60)
    #plt.ylim(0,4000)
    
    ax2 = ax1.twinx()
    z = [x+0.5 for x in ind]
    ax2.plot(z, pop10['pop']/1000000, label = 'Population', linewidth = 4, color = plt.rcParams['axes.color_cycle'][4])
    ax2.set_ylabel('Population in Millions')
    
    ax1.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 5))
    ax2.set_yticks(np.linspace(ax2.get_ybound()[0], ax2.get_ybound()[1], 5))
    #ax2.set_ylim(0,9.1)
    
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc=1)
    
    
    plt.gcf().subplots_adjust(bottom=0.24)
    
    plt.title('10 Most Mentioned US Cities in Jeopardy (1983-2016)')
    #plt.show()
    plt.savefig('top10cities.png', dpi=500)

def jep_sport_word_count():
    start = time.clock()
    
    # 36x faster to import the csv rather than an xlsx file
    jep_df = pd.read_csv('total_scrape_1.csv')
    sports5 = {'baseball':140, 'basketball':69, 'soccer':20, 'football':96, 'hockey':98}
    
    categories = list(jep_df['Category'])
    lc_cats = [w.lower() for w in categories]
    answers = list(jep_df['Answers'])
    lc_answers = [w.lower() for w in answers]
    clues = list(jep_df['Clues'])
    lc_clues = [w.lower() for w in clues]
    
    jep_df['lc_clues'] = lc_clues
    jep_df['lc_answers'] = lc_answers
    jep_df['lc_cats'] = lc_cats
    
    sport_counts = []
    sport_counts.append(['Sport', 'Age', 'Answers', 'Clues', 'Categories'])

    for sport in sports5:

        answer_count = jep_df.lc_answers.str.contains(sport).sum()
        clue_count = jep_df.lc_clues.str.contains(sport).sum()
        cat_count = jep_df.lc_cats.str.contains(sport).sum()/5
        
        age = sports5[sport]
        
        sport_counts.append([sport, age, answer_count, clue_count, cat_count])
        
    sport_results = pd.DataFrame(sport_counts, columns = sport_counts[0])
    sport_results.to_csv('sport_results.csv')
    
    end = time.clock()
    print (end-start)

    sport_results = pd.read_csv('sport_results.csv', skiprows=1)
    
    sport_results['total_mentions'] = sport_results['Answers'] + sport_results['Clues']  + sport_results['Categories'] 
    sport_results = sport_results.sort_values(by = 'total_mentions', ascending=False)
    
    ind = np.arange(5)
    fig, ax1 = plt.subplots()
    ax1.bar(ind, sport_results['Answers'], color = '#803E75', label = 'Answers', edgecolor = 'k', alpha = 0.8)
    ax1.bar(ind, sport_results['Clues'], bottom = sport_results['Answers'], color ='#00538A', label = 'Clues', edgecolor = 'k', alpha = 0.8)
    ax1.bar(ind, sport_results['Categories'], bottom = sport_results['Answers']+sport_results['Clues'], color = '#C10020', label = 'Categories', edgecolor = 'k', alpha = 0.8)
    
    plt.xlabel('Sport')
    plt.ylabel('Number of Mentions')
    cities = list(sport_results['Sport'])
    cities = [str(x) for x in cities]
    y = [x+0.25 for x in ind]
    plt.xticks(y, cities, rotation=60)
    #plt.ylim(0,4000)
    
    ax2 = ax1.twinx()
    z = [x+0.5 for x in ind]
    ax2.plot(z, sport_results['Age'], label = 'Age of Professional League', linewidth = 4, color = 'k')# marker = 'D', markeredgecolor = 'k')
    ax2.set_ylabel('Age of League (Years)')
    
    ax1.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 5))
    ax2.set_yticks(np.linspace(ax2.get_ybound()[0], ax2.get_ybound()[1], 5))
    #ax2.set_ylim(0,150)
    
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc=1)
   # plt.legend()
     
    plt.gcf().subplots_adjust(bottom=0.18)
    
    plt.title('Mentions of Top 5 American Sports in Jeopardy w/ Professional League Ages')
    #plt.show()
    plt.savefig('sports5.png', dpi=500)


def jep_word_hists():
    jep_df = pd.read_csv('total_scrape_1.csv')
    
    categories = list(jep_df['Category'])
    answers = list(jep_df['Answers'])
    clues = list(jep_df['Clues'])

    word_streams = [categories, clues, answers]  
    #pdb.set_trace()
    
    vocab_names = ['categories', 'answers', 'clues']
    i = 0
    for word_list in word_streams:
            
        words = [w.lower() for w in word_list]
        words = [word for word in words if word not in stopwords.words('english')]
        globals()[vocab_names[i]+'_vocab'] = sorted(set(words))
        i = i+1
        
def jep_pp():
    jep_df = pd.read_csv('total_scrape_1.csv')
    
    categories = list(jep_df['Category'])
    lc_cats = [w.lower() for w in categories]
    answers = list(jep_df['Answers'])
    lc_answers = [w.lower() for w in answers]
    clues = list(jep_df['Clues'])
    lc_clues = [w.lower() for w in clues]
    
    jep_df['lc_clues'] = lc_clues
    jep_df['lc_answers'] = lc_answers
    jep_df['lc_cats'] = lc_cats
    
    categories = list(jep_df['Category'])
    answers = list(jep_df['Answers'])
    clues = list(jep_df['Clues'])

    answer_count = jep_df.lc_answers.str.contains('potent potables').sum()
    clue_count = jep_df.lc_clues.str.contains('potent potables').sum()
    cat_count = jep_df.lc_cats.str.contains('potent potables').sum()/5
    
    return(answer_count, clue_count, cat_count)
    
x,y,z = jep_pp()
    
