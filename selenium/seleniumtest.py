from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://identidad.mtess.gov.py/alumno/register.php")

web_element = driver.find_element(By.NAME,'value_cedula_1')
web_element.send_keys("4641375" + Keys.ENTER)

time.sleep(30)
