from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://github.com/")

sing_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div/div[2]/a")
sing_in.click()

sleep(1)

try:
    email = driver.find_element(By.ID, "login_field")
    passwd = driver.find_element(By.ID, "password")
except Exception as e:
    print("Erro ao fazer login: ", e)

email.send_keys("dudumacedofelix613@gmail.com")
passwd.send_keys("EduMFT134")

login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/main/div/div[4]/form/div/input[12]")
login_btn.click()

user_btn = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")
user_btn.click()

sleep(1)
exit_btn = driver.find_element(By.CSS_SELECTOR, ".logout-form")
exit_btn.click()

driver.quit()