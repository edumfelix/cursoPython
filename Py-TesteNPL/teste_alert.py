from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep
driver = webdriver.Firefox()
driver.get("https://selenium.dunossauro.live/exercicio_12.html")
A = Alert(driver)

sleep(1)

input_name = driver.find_element(By.XPATH, "//*[@name='nome']")
input_name.click()
A.send_keys("Teste")
A.accept()

input_email = driver.find_element(By.XPATH, "//*[@name='email']")
input_email.click()
A.send_keys("Teste")
A.accept()

input_signo = driver.find_element(By.XPATH, "//*[@name='signo']")
input_signo.click()
A.send_keys("Teste")
A.accept()

btn_enviar = driver.find_element(By.XPATH, "//*[@value='Enviar']").click

driver.quit()