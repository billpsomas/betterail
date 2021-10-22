from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from time import sleep, strftime
from random import randint
import pandas as pd
import re
import pdb

# The chromedriver path
# Replace the path according to where chromedriver is located in your PC
chromedriver_path = 'C:/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path)
#sleep(randint(2,5))

driver.get('https://www2.ecotransit.org/calculation_extern.en.html')
#sleep(randint(2,5))

#cookies = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/a[1]')
#cookies.click()

#iframe = driver.find_element_by_xpath('/html/body/div[3]/div/div/section[2]/div/iframe')
#iframe.click()

#input_method = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/table/tbody/tr/td[2]')
#/html/body/div[3]/div/div/section[2]/div/iframe
#/html/body
#/html/body/div[2]/div[2]/div
#/html/body/div[2]/div[2]/div/table/tbody/tr/td[2]

input_method = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/table/tbody/tr/td[2]/div[2]/table/tbody/tr[1]/td')
print(input_method)

#input_method.click()
#input_method.select_by_visible_text('Extended')

#input_method = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/table/tbody/tr/td[2]/div[2]/table/tbody/tr[2]')
#input_method.click()



pdb.set_trace()



# select by visible text
#select.select_by_visible_text('Banana')

# select by value 
#select.select_by_value('1')