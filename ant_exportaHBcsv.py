import os
import shutil
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
 
driver = webdriver.Chrome()

# carpeta y ficheros para borrar, mover
ruta_descarga = 'c:/Users/onlin/Downloads'
ruta_final = 'c:/TFF/DOCS/ONLINE/STOCKS_EXTERNS'
fich1 = 'extract_produits.csv'
fich2 = 'extract_produits_tailles.csv'





url="http://triforfun.hiboutik.com/"
path_driver=os.chdir('C:/Users/onlin/AppData/Local/Programs/Python/Python311/Scripts')
                     

driver.maximize_window()
driver.get(url)

# texto_1 = driver.find_element(By.XPATH, '//form/div/select[contains(text(),"boutique")]')
# $x('//form/div/select')

botiga = driver.find_element(By.XPATH, '//select[@id="code_boutique"]')
botiga.send_keys("TRI FOR FUN, S.L.")

time.sleep(2)

# midle_name = driver.find_element(By.XPATH,'//input[@id="middlename"]')
# https://selectorshub.com/selectorshub/

usuari = driver.find_element(By.NAME,"login_user")
usuari.send_keys("comercial@triforfun.es")

time.sleep(1)

psswrd = driver.find_element(By.NAME,"pass_user")
psswrd.send_keys("tffpsswrd")

entrar = driver.find_element(By.XPATH, "//button[@type='submit']")
entrar.click()

entrar2 = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/ul/li[4]/form")
entrar2.click()

# la linea siguiente no da error pero la de click si, debe ser por que no esta visualizado el submenu
entrar3 = driver.find_element(By.XPATH, "//li/ul/li/form/button[@type='submit'][@value='Importar-Exportar']")
entrar3.click()

entrar4 = driver.find_element(By.XPATH, "/html/body/div[2]/nav/div/ul/li[4]/ul/li[7]/form")
entrar4.click()

exportar_datos = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[1]/h4/a")
exportar_datos.click()

time.sleep(3)

generar_csv1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/table/tbody/tr[7]/td[4]/form/button/span")
generar_csv1.click()

time.sleep(3)
descargar_csv1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/table/tbody/tr[7]/td[5]/a/button/span")
descargar_csv1.click()

time.sleep(3)
generar_csv2 = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/table/tbody/tr[9]/td[4]/form")
generar_csv2.click()
time.sleep(3)

descargar_csv2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/table/tbody/tr[9]/td[5]/a/button/span")
descargar_csv2.click()

print("ha pasado por descargar2")

time.sleep(10)


driver.quit()