from cmath import exp
from unicodedata import name
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

wait = WebDriverWait(driver, 40)
driver.switch_to.frame("iframe_MenuPrincipal")
driver.switch_to.frame("nmsc_iframe_IframeZoho_1")
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='https://reports.zoho.com/ZDBDataSheetView.cc?OBJID=1390984000000007513&STANDALONE=true&WIDTH=800&HEIGHT=600&INTERVAL=-1&REMTOOLBAR=true&INCLUDETITLE=true&INCLUDEDESC=true']"))
wait.until(EC.visibility_of_element_located((By.XPATH, "//td[.='Campus:']/../../tr/td/div/div[@value='Todos']")))

btn_todos = driver.find_element(By.XPATH, "//td[.='Campus:']/../../tr/td/div/div[@value='Todos']/div").click()

sleep(1)
btn_check_todos = driver.find_element(By.XPATH, '//div[@id="vmOptionList_Campus"]/div[@elname="optionDiv"]/ul[@class="multi_allOpt VMFilterValue VMFilterValueNew VMFilterValueMulti"]/li/span[@class="likeCheckBoxEl"]').click()
text_check_maracanau = driver.find_element(By.XPATH, '//li[@data-tip="Maracanau"]/span[2]').text
btn_check_maracanau = driver.find_element(By.XPATH, '//li[@data-tip="Maracanau"]/span[2]').click()
btn_check_ok = driver.find_element(By.XPATH, '//input[@elname="multiSelOk"]').click()

name_maracanau = driver.find_element(By.CSS_SELECTOR, 'div.ly-node:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > svg:nth-child(1) > g:nth-child(2) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1) > g:nth-child(2) > g:nth-child(2) > text:nth-child(3)')

try:
    if name_maracanau.text == text_check_maracanau:
        print("Teste OK")
    else:
        print("Teste Falhou")
        print(f'{name_maracanau.text} != {text_check_maracanau}')
except Exception as e:
    print("Erro: ", e)

driver.quit()
