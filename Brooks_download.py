import os
# debug import shutil
import time
# debug import selenium
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url="https://fasttrack.brooksrunning.com/authentication/login"
path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python312/Scripts')
                   
chrome_driver_path = "C:/Users/onlin/AppData/Local/Programs/Python/Python312/Scripts"

driver.maximize_window()

driver.get(url)

time.sleep(6)

# /html/body/epc-root/main/epc-auth-page/div/epc-auth-login/form/div[1]/input
usuari = driver.find_element(By.XPATH, '/html/body/epc-root/main/epc-auth-page/div/epc-auth-login/form/div[1]/input')
usuari.send_keys("comercial@triforfun.es")

time.sleep(2)
# /html/body/epc-root/main/epc-auth-page/div/epc-auth-login/form/div[2]/input
quinpassword = driver.find_element(By.XPATH,'/html/body/epc-root/main/epc-auth-page/div/epc-auth-login/form/div[2]/input')
quinpassword.send_keys("Tffbrooks2023")

time.sleep(2)

# /html/body/epc-root/main/epc-auth-page/div/epc-auth-login/form/button
sign_in = driver.find_element(By.XPATH, '/html/body/epc-root/main/epc-auth-page/div/epc-auth-login/form/button')
sign_in.click()

time.sleep(5)
Mislistas = driver.find_element(By.XPATH, '/html[1]/body[1]/epc-root[1]/epc-main-navigation[1]/epc-full-header[1]/nav[1]/ul[1]/li[1]/epc-nav-link[1]/a[1]')
# Mislistas = driver.find_element(BY.XPATH, '/html[1]/body[1]/epc-root[1]/main[1]/epc-browse[1]/section[1]/atx-aside-menu[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]')
Mislistas.click()
print("ha pasado por Mislistas")
time.sleep(1)

url_lista ="https://fasttrack.brooksrunning.com/lnk/OGY3OWM4OT"
driver.get(url_lista)

# listafw23 = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div[1]/div[2]/div[2]/span/span')
# time.sleep(1)

# listafw23 = driver.find_element(By.XPATH, ("/html[1]/body[1]/epc-root[1]/main[1]/epc-browse[1]/section[1]/div[1]/epc-product-list-page[1]/epc-dynamic-layout-builder[1]/epc-dynamic-collections-renderer[1]/epc-dynamic-collections-renderer[2]/epc-dynamic-elements-dropdown[1]/button[1]/fa-icon[1]/*[name()='svg'][1]/*[name()='path'][1]"))

# listafw23.click()

# css selector driver.findElement(By.cssSelector(".btn.btn-dropdown-trigger"))
# classname driver.findElement(By.className("btn btn-dropdown-trigger"))
# rodetamenu = driver.find_element(By.CLASS_NAME, 'btn btn-dropdown-trigger')
rodetamenu = driver.find_element(By.CSS_SELECTOR, "body > epc-root > main > epc-browse > section > div > epc-product-list-page > epc-dynamic-layout-builder > epc-dynamic-collections-renderer.row.align-items-center.my-3.ng-star-inserted > epc-dynamic-collections-renderer.col.d-flex.justify-content-end.order-3.ng-star-inserted > epc-dynamic-elements-dropdown > button > fa-icon > svg")

# abs path driver.findElement(By.xpath("/html[1]/body[1]/epc-root[1]/main[1]/epc-browse[1]/section[1]/div[1]/epc-product-list-page[1]/epc-dynamic-layout-builder[1]/epc-dynamic-collections-renderer[1]/epc-dynamic-collections-renderer[2]/epc-dynamic-elements-dropdown[1]/button[1]"))

rodetamenu.click()

print("esta en rodeta asterics menu")
time.sleep(1)


download_data = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/atx-dropdown-item[3]/div/fa-icon/svg')
# download_data = driver.find_element(BY.XPATH, '/html/body/div/div[2]/div/div/atx-dropdown-item[3]')
download_data.click()
time.sleep(10)


time.sleep(1)

keyboard.press_and_release("tab")
keyboard.press_and_release("tab")
keyboard.press_and_release("enter")
time.sleep(1)
print("ha guardado el fichero en Descargas")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#AQUI ACABA 
driver.quit()