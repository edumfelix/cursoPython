from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://sei.ifce.edu.br/sei/controlador_externo.php?acao=usuario_externo_logar&acao_origem=usuario_externo_enviar_cadastro&id_orgao_acesso_externo=0")

email = driver.find_element(By.ID, "txtEmail")
email.send_keys("henriquefisicoquimico@gmail.com")

passwd = driver.find_element(By.ID, "pwdSenha")
passwd.send_keys("3YCquJNS")

confirm = driver.find_element(By.ID, "sbmLogin")
confirm.click()

click_exit = driver.find_element(By.ID, "lnkSairSistema")
click_exit.click()
