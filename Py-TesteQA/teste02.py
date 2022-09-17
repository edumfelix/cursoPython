from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://amazon.com.br")

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("celular")
search.send_keys(Keys.RETURN)

time.sleep(1)
resultado = driver.find_element(By.CSS_SELECTOR, ".a-color-state")

driver.quit()

