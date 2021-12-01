from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
print('Opening Chrome')

driver.get('https://10fastfingers.com/advanced-typing-test/english')
delay = 10

cont = input("Press Enter after accepting cookies")
# Accept cookies
# WebDriverWait(driver, delay).until(expected_conditions.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
# driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").send_keys(Keys.ENTER)

sleep(2)
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")
k = len(words)
print(k)
for i in range(k):
    driver.find_element_by_id("inputfield").send_keys(words[i] + ' ')
    sleep(0.01)
