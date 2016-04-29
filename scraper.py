# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:48:40 2015

@author: cwal3
"""

from selenium import webdriver

import pandas as pd

questions = []

driver = webdriver.Chrome()
base_url = 'http://www.j-archive.com/showgame.php?game_id='
#for i in range(1,5162):
game_url = base_url + str(1)
driver.get(game_url)
    
    
rounds = ['jeopary_round', 'double_jeopardy_round', 'final_jeopardy_round']

# 6 tr elements in each table class=round    

for div_e in driver.find_elements_by_id('div'): # select the url in href for all a tags(links) look, comments can go anywhere(ish)
    print team
    round_one = team.get_attribute('onmouseover')
    round_two = 
    round_final = 
    print q_string
    
    questions.append(q_string)

driver.close()
driver.quit()


    
    

        
    
