from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://selenium.dunossauro.live/aula_11_d.html")

driver.switch_to.frame("iframe")

input_name = driver.find_element(By.ID, "nome")
input_name.send_keys("teste")

input_email = driver.find_element(By.ID, "email")
input_email.send_keys("teste@teste.com")

input_senha = driver.find_element(By.ID, "senha")
input_senha.send_keys("teste")

btn_enviar = driver.find_element(By.ID, "btn").click()

driver.quit()