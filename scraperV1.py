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

rounds_longform = ['jeopardy_round', 'double_jeopardy_round', 'final_jeopardy_round']

"""
NOTE: There are some blank questions I think? So make sure there is an error
exception handle for those cases.

Structure of question/answer format in HTML
column,row

1. Round 1
    1. div id="jeopardy_round"
        1. table class="round"
            1. tbody
                1. tr - Leads to Category Names
                    1. td class="category"
                        1. table
                            1. tbody
                                1. tr - Leads to category name in column 1
                                    1. td class"category_name"
                2. tr - Leads to answer/clue in row 1
                    1. td class="clue"
                        1. table
                            1. tbody
                                1. tr
                                    1. td - Leads to question in column 1
                                        1. dov onmouseover="toggle...
                3. tr - Leads to answer/clue in row 2
                    1. td class="clue"
                        1. table
                            1. tbody
                                1. tr
                                    1. td - Leads to question in column 1
                                        1. dov onmouseover="toggle...
                4. tr - Leads to answer/clue in row 3
                    1. td class="clue"
                        1. table
                            1. tbody
                                1. tr
                                    1. td - Leads to question in column 1
                                        1. dov onmouseover="toggle...
                5. tr - Leads to answer/clue in row 4
                    1. td class="clue"
                        1. table
                            1. tbody
                                1. tr
                                    1. td  - Leads to question in column 1
                                        1. dov onmouseover="toggle...
                6. tr - Leads to answer/clue in row 5
                    1. td class="clue"
                        1. table
                            1. tbody
                                1. tr
                                    1. td - Leads to question in column 1
                                        1. dov onmouseover="toggle...
2. Round 2
3. Round 3
"""

i = 1 # table iterator
j = 2 # first tr iterator
n = 2 # td iterator
m = 1 # second tr iterator
data =  driver.find_element_by_xpath('//*[@id="jeopardy_round"]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div').get_attribute('outerHTML')#.text#.get_attribute('innerHTML')
print data
#data =  driver.find_elements_by_xpath('//*[@id="jeopardy_round"]/table[1]/tbody/tr[2]/td[1]')


#for div_e in driver.find_element_by_class_name('correct_response'):
i = 0
#for data in driver.find_element_by_class_name("clue").text:
#    print data
#    print i
#    i = i + 1
    
#for data in driver.find_elements_by_tag_name("table"):
#    em = data.find_element_by_partial_link_text('div onmouseover')
#    print em
#    i = i + 1
    



       # print 'hey'
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


    
    

        
    
