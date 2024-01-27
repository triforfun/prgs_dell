import os
# debug import shutil
import time
# debug import selenium
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url="https://comercialudrab2b.elasticsuite.com/"
path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python311/Scripts')
                   
chrome_driver_path = "C:/Users/onlin/AppData/Local/Programs/Python/Python311/Scripts"

driver.maximize_window()
# driver.minimize_window()
driver.get(url)

time.sleep(1)

# usuari = driver.find_element(By.ID,'elasticScramble_splash_login_username_input')
usuari = driver.find_element(By.XPATH, '/html/body/div[12]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/form/div[1]/div[2]/div/input')
usuari.send_keys("info@triforfun.es")

time.sleep(2)

# quinpassword = driver.find_element(By.XPATH, '/html/body/div[12]/div/div[2]/div/div/div[1]/div[3]/div/form/div[3]/div/div[2]/div/div[2]/input')
quinpassword = driver.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/form/div[2]/div[2]/div/input')
quinpassword.send_keys("HokaTff2022")

time.sleep(2)

# login = driver.find_element(By.XPATH, "/html/body/div[12]/div/div[2]/div/div/div[1]/div[3]/div/form/div[5]/span")
login = driver.find_element(By.XPATH, '/html/body/div[12]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/form/button')
login.click()

time.sleep(2)

marca = driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/div/div[1]/div/div/div[2]/div[3]/div/div/div/div[1]/img')
marca.click()

time.sleep(2)

#-------------------------------
#-------------------------------
# aqui comença ARENA FW23

marca = driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/div/div[1]/div/div/div[2]/div[3]/div/div/div/div[2]/img')
marca.click()

time.sleep(3)


arenaFW23 = driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/div/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/p')
arenaFW23.click()
print("ha pasado por seasonFW23")
time.sleep(1)

menuorderfw = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div[1]/div[2]/div[2]/span/span')

time.sleep(1)
menuorderfw.click()

exportArenaFW23 = driver.find_element(By.ID, 'dijit_MenuItem_6_text')
exportArenaFW23.click()

print("ha pasado por exportArena fw23")
time.sleep(1)
exportacatArenafw23 = driver.find_element(By.ID, '"uniqName_18_5_full_catalog')
# exportacatArenafw23 = driver.find_element(By.XPATH, '/html/body/div[61]/div[2]/div/form/div[2]')
exportacatArenafw23.click()
time.sleep(1)
allproductArenafw23 = driver.find_element(By.ID, 'uniqName_14_5_all')
allproductArenafw23.click()

time.sleep(2)

keyboard.press_and_release("tab")
keyboard.press_and_release("tab")
keyboard.press_and_release("tab")
keyboard.press_and_release("enter")
time.sleep(10)
print("ha pasado por exportar XLS Arena FW23")


# **********************
# **********************
# aqui acaba ARENA FW23
driver.quit() 