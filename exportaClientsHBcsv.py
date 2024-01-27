import shutil
from os import remove
from pathlib import Path

import os
import time
import keyboard

from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python312/Scripts')
                     
chrome_driver_path = "C:/Users/onlin/AppData/Local/Programs/Python/Python312/Scripts"

# carpeta y ficheros para borrar, mover
# ruta_descarga = 'c:/Users/onlin/Downloads' Firefox per defecte descarrega aqui sense dir res
ruta_final = 'c:/TFF/GESTIO/HIBOUTIK/CLIENTES/extract_clients.csv'
fich1 = 'c:/Users/onlin/Downloads/extract_clients.csv'

if Path(fich1).is_file():
    print(fich1)
    print("ha encontrado el fichero de origen")
    os.remove(fich1)
else:
    print("NO HA ENCONTRADO EL FICHERO ", fich1)    

url="http://triforfun.hiboutik.com/"
path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python312/Scripts')
                   
driver.get(url)


keyboard.press_and_release("tab")
time.sleep(2)

keyboard.press_and_release("tab")
time.sleep(2)

keyboard.press_and_release("tab")
time.sleep(2)

usuari = driver.find_element(By.NAME,"login_user")
usuari.send_keys("comercial@triforfun.es")

time.sleep(1)

psswrd = driver.find_element(By.NAME,"pass_user")
psswrd.send_keys("tffpsswrd")

entrar = driver.find_element(By.XPATH, "//button[@type='submit']")
entrar.click()

clickmenuClientes = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/ul/li[3]/form/button/span")
clickmenuClientes.click()

# la linea siguiente no da error pero la de click si, debe ser por que no esta visualizado el submenu
clickExportar = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form[2]/button/span")
clickExportar.click()

clickDescargar = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/center/form/button/strong")
clickDescargar.click()

time.sleep(10)
driver.quit()

if Path(ruta_final).is_file():
    print(ruta_final)
    print("ha encontrado el fichero de destino")
    os.remove(ruta_final)
else:
    print("NO HA ENCONTRADO EL FICHERO ", ruta_final)    

shutil.move(fich1, ruta_final)