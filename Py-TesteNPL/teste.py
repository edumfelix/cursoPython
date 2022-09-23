from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

sleep(20)

try:
    # wait = WebDriverWait(driver, 20)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//td[.='Campus:']/../../tr/td/div/div[@value='Todos']/div/input"))).click()
    click_todos_btn = driver.find_element(By.XPATH, "//td[.='Campus:']/../../tr/td/div/div[@value='Todos']/div/input").click()
except Exception as e:
    print(e)

driver.quit()

"""
1. Clicar em Todos
2. Clicar em Maracanaú
3. Clicar em OK
4. Comparar resultado com pesquisa
"""