from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration1.html"


driver = webdriver.Chrome()

try:
    driver.get(url)
    num1 = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div[1]/input")
    num1.send_keys("123")
    num2 = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div[2]/input")
    num2.send_keys("123")
    num3 = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/div[3]/input")
    num3.send_keys("123")
    button = driver.find_element(By.XPATH,"/html/body/div/form/button")
    button.click()
    time.sleep(3)
    registration = driver.find_element(By.XPATH,"/html/body/div/h1")
    text1 = registration.text
    assert "Congratulations! You have successfully registered!"== text1
finally:
    time.sleep(5)
    driver.quit()