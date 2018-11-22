from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome()
driver.get(('https://soft2.herokuapp.com/'))

driver.execute_script("ingresar();")

username = driver.find_element_by_name("codigou")
password = driver.find_element_by_name("clave")

username.send_keys('1111')
password.send_keys('admin')

driver.find_element_by_id("a1").click()

username = driver.find_element_by_name("crearsession")
username.send_keys('785')

driver.find_element_by_name("bseccion").click()
time.sleep(1)
driver.find_element_by_name("selectedsecc").click()
time.sleep(2)
driver.find_element_by_name("salir").click()
time.sleep(3)
driver.execute_script("ingresar();")

username = driver.find_element_by_name("codigou")
password = driver.find_element_by_name("clave")

username.send_keys('2555555')
password.send_keys('gg')

driver.find_element_by_id("a1").click()
driver.find_element_by_id("1").click()
time.sleep(1)
driver.find_element_by_name("curso").click()
time.sleep(1)
driver.find_element_by_name("prof").click()
time.sleep(1)
driver.find_element_by_name("aseso").click()
time.sleep(1)
driver.find_element_by_name("aseso").click()
time.sleep(4)
driver.find_element_by_name("aseso").click()
time.sleep(4)
driver.find_element_by_name("cance").click()
