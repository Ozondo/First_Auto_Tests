from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/find_xpath_form"

driver = webdriver.Chrome()

try:
    driver.get(url)
    name = driver.find_element(By.XPATH,"//body//div//div[1]/input")
    name.send_keys("ivan")
    surname = driver.find_element(By.XPATH,"//body//div[2]/input")
    surname.send_keys("ivanov")
    city = driver.find_element(By.XPATH,"//body//div[3]/input")
    city.send_keys("ivanovo")
    country = driver.find_element(By.XPATH,"//body//div[4]/input")
    country.send_keys("ivanovichi")
    button = driver.find_element(By.XPATH,"/html/body/div/form/div[6]/button[3]")
    button.click()
finally:
    time.sleep(2)
    driver.quit()