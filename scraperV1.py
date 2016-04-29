# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:48:40 2015

@author: cwal3
"""

from selenium import webdriver

import pandas as pd

game = []
answers = []
clues = []
clues.append(['clue'])
answers.append(['answer'])

driver = webdriver.Chrome()
base_url = 'http://www.j-archive.com/showgame.php?game_id='
#for i in range(1,5162):
game_url = base_url + str(1)
driver.get(game_url)
    
"""
id structure
clue_J_2_1 = jeopardy, column 2, clue 1
clue_DJ_3_2 = double jeopardy, column 3, clue 2
"""

rounds = ['J', 'DJ']

for round_type in rounds:
    for i in range(1,7):
        for j in range(1,6):
            clue_id = 'clue_'+round_type+'_'+str(i)+'_'+str(j)
            clue = driver.find_element_by_id(clue_id)
            clue_value = clue.text
            #clue_str = str(clue.find_element_by_class('clue_text'))
            print clue_value
            clues.append(clue_value)
            
        
driver.get(game_url)
for div_e in driver.find_element_by_class_name('correct_response'):
    print div_e
                    #try:
    #print q_mess
#        q_string = q_mess.value
#        answers.append(q_string)
#        print q_string
#    except AttributeError:
#        print q_string
#    
#for div_e in driver.find_elements_by_tag_name('div'): 
#    q_mess = div_e.find_element_by_class_name('em.correct answer')
#    print q_mess
#    try:
#        q_string = str(q_mess.get_attribute('em'))
#        answers.append(q_string)
#        print q_string
#    except AttributeError:
#        print q_string  

driver.close()
driver.quit()


    
    

        
    
