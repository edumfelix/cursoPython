from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://amazon.com.br")

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("celular")
search.send_keys(Keys.RETURN)

#//div/span[.='\"celular\"']
result = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/span/div/h1/div/div[1]/div/div/span[3]")
print(result)
# if search.text  == result.text:
#   print('True')
# else:
#   print('ERROR!')

# browser.quit()