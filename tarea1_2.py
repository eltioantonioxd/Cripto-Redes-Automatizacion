# -*- coding: utf-8 -*-
import string
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.ovs.it/login")
time.sleep(5)
base62 = string.ascii_letters + string.digits 
sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
ascii_256 = "@#~¥§«Æ¼ñÑá^ø=()’\($þ”ßÐ‡‰―‼⁊‹¢"
arabic = "ء آ أ ؤ ئ ا ب ة ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ل م ن ه و ي ً ٌ ٍ َ ُ ِ ّ ْ ٔ ٰ ټ پ ځ څ چ ډ ړ ږ ژ ښ ک ګ گ ڼ ی ۍ ې ﭖ ﭗ ﭘ ﭙ ﭺ ﭻ ﭼ ﭽ ﮊ ﮋ ﮎ ﮏ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﯤ ﯥ ﯦ ﯧ ﯼ ﯽ ﯾ ﯿ ﺀ ﺍ ﺎ ﺏ ﺐ ﺑ ﺒ ﺓ ﺔ ﺕ ﺖ ﺗ ﺘ ﺙ ﺚ ﺛ ﺜ ﺝ ﺞ ﺟ ﺠ ﺡ ﺢ ﺣ ﺤ ﺥ ﺦ ﺧ ﺨ ﺩ ﺪ ﺫ ﺬ ﺭ ﺮ ﺯ ﺰ ﺱ ﺲ ﺳ ﺴ ﺵ ﺶ ﺷ ﺸ ﺹ ﺺ ﺻ ﺼ ﺽ ﺾ ﺿ ﻀ ﻁ ﻂ ﻃ ﻄ ﻅ ﻆ ﻇ ﻈ ﻉ ﻊ ﻋ ﻌ ﻍ ﻎ ﻏ ﻐ ﻑ ﻒ ﻓ ﻔ ﻕ ﻖ ﻗ ﻘ ﻝ ﻞ ﻟ ﻠ ﻡ ﻢ ﻣ ﻤ ﻥ ﻦ ﻧ ﻨ ﻩ ﻪ ﻫ ﻬ ﻭ ﻮ ﻱ ﻲ ﻳ ﻴ"
letters = base62 + sub_s + ascii_256 + arabic
for x in range(100):
    usr = driver.find_element_by_id("login-form-email")
    usr.clear()
    usr.send_keys("espinabrayan@gmail.com")
    psw = driver.find_element_by_id("login-form-password")
    str = ''.join(random.choice(letters) for i in range(random.randrange(8,255)))
    psw.send_keys(str)
    print(str)
    clk = driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div[1]/div/div/div/form/button").submit()
    time.sleep(2)
    psw.clear()
driver.close()