# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:48:40 2015

@author: cwal3
"""

from selenium import webdriver
import pdb
import pandas as pd

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

id structure
clue_J_2_1 = jeopardy, column 2, clue 1
clue_DJ_3_2 = double jeopardy, column 3, clue 2
"""

game = []
answers = []
clues = []

driver = webdriver.Chrome()
base_url = 'http://www.j-archive.com/showgame.php?game_id='
#for g_id in range(1,5162):
g_id = 5162
game_url = base_url + str(5162)
driver.get(game_url)
    


rounds = ['J', 'DJ']

for round_type in rounds:
    for i in range(1,7):
        for j in range(1,6):
            clue_id = 'clue_'+round_type+'_'+str(i)+'_'+str(j)
            clue = driver.find_element_by_id(clue_id)
            clue_value = clue.text
            clues.append(clue_value)
clue_length = len(clues)
game_id = []
rounds_longform = ['jeopardy_round', 'double_jeopardy_round']#, 'final_jeopardy_round']
cat_names = []
for jround in rounds_longform:
    for i in range(1,7):
        cat_name = driver.find_element_by_xpath('//*[@id="'+jround+'"]/table[1]/tbody/tr[1]/td['+str(i)+']/table/tbody/tr[1]/td').text
        cat_names.append(cat_name)

categories = []
for cat in cat_names:
    for i in range(0,5):
        categories.append(cat)

for i in range(0,clue_length):
    game_id.append(g_id)
    


# use sdata = str(data) to get a string
# then use ans_start = sdata.find('correct_response') to get the start of that string
# and ans_end = sdata.find('</em>') to find the end of the answer string
# from there you can do ans_str = sdata[ans_start+23:ans_end]
# could also iterate through for questions in this manner
# just need to finalize the tr/td i/j looping structure and we should be in business


for jround in rounds_longform:
    for i in range(1,7):
        for j in range(2,7):
            current_xpath = '//*[@id="'+jround+'"]/table[1]/tbody/tr['+str(j)+']/td['+str(i)+']/table/tbody/tr[1]/td/div'
            print current_xpath
            data =  driver.find_element_by_xpath('//*[@id="'+jround+'"]/table[1]/tbody/tr['+str(j)+']/td['+str(i)+']/table/tbody/tr[1]/td/div').get_attribute('outerHTML')
            #print data
            #sdata = str(data)
            ans_start = data.find('correct_response')+23
            #print sdata
            ans_end = data.find('</em>')
            ans_uni = data[ans_start:ans_end]
            ans_str = str(ans_uni)
            answers.append(ans_str)



driver.close()
driver.quit()

clues_series = pd.Series(clues)
answers_series = pd.Series(answers)

games = pd.DataFrame(clues_series, columns=['Clues'])

games['Answers'] = answers_series

games['G_ID'] = game_id
games['Category'] = categories

games.to_excel('proof_of_concept.xls')