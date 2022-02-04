from multiprocessing.connection import wait
import os
from asyncore import loop
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
while True:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('') #paste the video link here
    os.system("kill chromium")
