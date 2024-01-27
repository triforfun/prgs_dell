# descarrega els fitxers .csv de sailfish primer i de blunae després
import requests
import os
import time
from selenium import webdriver
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# url="https://www.sailfish.com/backend/export/index/Availability.csv?feedID=23&hash=f6c634e3edfb9093ff5bffc94f39ad8b"
url="https://b2b.sailfish.com/backend/export/index/Availability.csv?feedID=23&hash=f6c634e3edfb9093ff5bffc94f39ad8b"
path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python311/Scripts')
                    
# driver.maximize_window()
driver.minimize_window()
driver.get(url)

myfile = requests.get(url)
open('C:/TFF/DOCS/ONLINE/STOCKS_EXTERNS/Availability.csv', 'wb').write(myfile.content)

time.sleep(1)

url2 ="http://descargas.blunae.es/informe-maesarti.csv"
driver.get(url2)
time.sleep(1)

driver.quit() 
