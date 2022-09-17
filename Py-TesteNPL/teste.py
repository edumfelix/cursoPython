from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://prpi.ifce.edu.br/nl/app_Login/")

try:
    login_with_cpf = driver.find_element(By.ID, "id_sc_field_login")
    passwd = driver.find_element(By.ID, "id_sc_field_pswd")
except Exception as e:
    print("Erro ao fazer login: ", e)

login_with_cpf.send_keys("60958760365")
passwd.send_keys("EduMFT134")

login_btn = driver.find_element(By.XPATH, "//input[@class='button']").click()

sleep(60)

input_campus = driver.find_element(By.XPATH, "//td[.='Campus:']/../../tr/td/div/div[@value='Todos']/div/input[@class='dComboTextInput widthClass']").click()

"""
1. Clicar em Todos
2. Clicar em Maracanaú
3. Clicar em OK
4. Comparar resultado com pesquisa
"""