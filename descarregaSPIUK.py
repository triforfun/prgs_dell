import os
# debug import shutil
import time
# debug import selenium
# debug import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
# debug from selenium.webdriver.chrome.service import Service
# debug from selenium.webdriver.common.keys import Keys
# debug from selenium.webdriver.support.ui import WebDriverWait
# debug from selenium.webdriver.support import expected_conditions as EC
# debug from selenium.webdriver.common.action_chains import ActionChains
# debug from selenium.common.exceptions import NoSuchElementException, TimeoutException

# from selenium.webdriver.chrome.service import Service as ChromeService
# debug from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

url="https://www.spiuk.pro/es/"
path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python311/Scripts')                    

driver.maximize_window()
driver.get(url)

delegacion = driver.find_element(By.NAME,"Delegacion")
delegacion.send_keys("5962")

time.sleep(1)

Clave = driver.find_element(By.NAME,"Clave")
Clave.send_keys("03130524")

acceder = driver.find_element(By.XPATH, "/html/body/main/div/div/form/div[3]/button")
acceder.click()

time.sleep(10)

descargas = driver.find_element(By.XPATH, "/html/body/header/div[1]/nav/div/ul/li[3]/a")
descargas.click()

time.sleep(3)

stock_csv = driver.find_element(By.XPATH, "/html/body/header/div[1]/nav/div/ul/li[3]/ul/li[1]/a")
stock_csv.click()

# url2 ="https://www.orbea.com/es-es/kide/available/csv/"
# driver.get(url2)
time.sleep(1)

driver.quit()