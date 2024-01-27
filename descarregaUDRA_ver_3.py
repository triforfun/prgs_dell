            
import os
# debug import shutil
import time
# debug import selenium
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url="https://comercialudrab2b.elasticsuite.com/"
path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python312/Scripts')
                   
chrome_driver_path = "C:/Users/onlin/AppData/Local/Programs/Python/Python312/Scripts"

driver.maximize_window()
# driver.minimize_window()
driver.get(url)

time.sleep(6)

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
# AQUI COMENÇA DESCARREGA SS23

#                                           /html/body/div[12]/div[3]/div/div[2]/div[1]/div/div/div[4]/div/div/div[1]/div[2]/p
#                                           /html/body/div[12]/div[3]/div/div[2]/div[1]/div/div/div[4]/div/div/div[1]/div[2]/p
seasonss23 = driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/div/div[2]/div/div/div/div[4]/div/div/div[1]/div[2]/p')
seasonss23.click()
print("ha pasado por seasonSS23")
time.sleep(3)

menuorder = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div[1]/div[2]/div[2]/span/span')
# ESTO NO DA ERROR PER EL .click siguiente SI    menuorder = driver.find_element(By.ID, 'dijit_form_Button_5')
time.sleep(3)
menuorder.click()

exportaxlsx = driver.find_element(By.ID, 'dijit_MenuItem_6_text')
exportaxlsx.click()

print("ha pasado por exportaxlsx")
time.sleep(3)
exportacat = driver.find_element(By.ID, 'uniqName_14_3_full_catalog')
exportacat.click()
time.sleep(1)
allproduct = driver.find_element(By.ID, 'uniqName_14_3_all')
allproduct.click()

time.sleep(1)

# exportarSS23 = driver.find_element(By.ID, 'dijit_form_Button_24')
# exportarSS23 = driver.find_element(By.ID, 'dijit_form_Button_48')



# exportarSS23.click()
keyboard.press_and_release("tab")
keyboard.press_and_release("tab")
keyboard.press_and_release("enter")
time.sleep(3            
           )





# webdriver.ActionChains(driver).move_to_element(exportarSS23).click(exportarSS23).perform()
print("ha pasado por exportarSS23")

time.sleep(4)

# clicar al logo de hoka per retornar a escollir cataleg i escollir FW23
tornaraHoka = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div[1]/div[1]/div[1]')
tornaraHoka.click()
print("ha pasado por tornar a Hoka un altre cop")

time.sleep(3)


# time.sleep(5)


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#AQUI ACABA SS23

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#AQUI COMENÇA FW23

time.sleep(3)


seasonFW23 = driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/div/div[2]/div/div/div/div[4]/div/div/div[1]/div[1]/p')
seasonFW23.click()
print("ha pasado por seasonFW23")
time.sleep(1)

menuorderfw = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div[1]/div[2]/div[2]/span/span')
# ESTO NO DA ERROR PER EL .click siguiente SI    menuorder = driver.find_element(By.ID, 'dijit_form_Button_5')
time.sleep(1)
menuorderfw.click()

exportaxlsxFW23 = driver.find_element(By.ID, 'dijit_MenuItem_6_text')
exportaxlsxFW23.click()

print("ha pasado por exportaxlsx fw23")
time.sleep(1)
exportacatfw23 = driver.find_element(By.ID, 'uniqName_14_4_full_catalog')
exportacatfw23.click()
time.sleep(1)
allproductfw23 = driver.find_element(By.ID, 'uniqName_14_4_all')
allproductfw23.click()

time.sleep(1)

# exportarFW23 = driver.find_element(By.ID, 'dijit_form_Button_55')
# exportarFW23 = driver.find_element(By.XPATH, 'body[1]/div[107]/div[3]/span[2]/span[1]')
# exportarFW23 = driver.find_element(By.XPATH, '/html/body/div[81]/div[3]/span[2]/span/span')
# exportarFW23 = driver.find_element(By.XPATH, '//*[@id="dijit_form_Button_24_label"]')
# webdriver.ActionChains(driver).move_to_element(exportarFW23).click(exportarFW23).perform()
# exportarFW23.click()

keyboard.press_and_release("tab")
keyboard.press_and_release("tab")
keyboard.press_and_release("tab")
keyboard.press_and_release("enter")
time.sleep(1)
print("ha pasado por exportarFW23")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#AQUI ACABA FW23

# clicar al logo de hoka per retornar a escollir cataleg i escollir FW23
tornaraHoka = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div[1]/div[1]/div[1]')
tornaraHoka.click()
print("ha pasado por tornar a Hoka un altre cop")
time.sleep(1)

# ***********************
# ***********************
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
exportacatArenafw23 = driver.find_element(By.ID, 'uniqName_14_5_full_catalog')
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