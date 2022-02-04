from multiprocessing.connection import wait
import os
from asyncore import loop
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
while True:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://youtu.be/4UKGj_b0_wg') 
    os.system("kill chromium")

