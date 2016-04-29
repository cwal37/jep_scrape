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
    

for team in driver.find_elements_by_tag_name('div'): # select the url in href for all a tags(links) look, comments can go anywhere(ish)
    print team
    q_string = team.get_attribute('onmouseover')
    print q_string
    
    questions.append(q_string)

driver.close()
driver.quit()


    
    

        
    
