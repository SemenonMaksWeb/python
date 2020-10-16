from selenium import webdriver
from confing import *
webdriver = webdriver.Chrome("./chromedriver.exe")
webdriver.get(NAME_SITE[0])
menu_games = webdriver.find_element_by_css_selector(".s_au .s_av > .d-b > .t-t-u d-b .s_aw")
print(menu_games)
 