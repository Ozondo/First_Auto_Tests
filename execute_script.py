from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

url = "http://suninjuly.github.io/execute_script.html"

driver = webdriver.Chrome()

try:
    driver.get(url)
    x = int(driver.find_element(By.ID,"input_value").text)

    answer = driver.find_element(By.ID,"answer")
    answer.send_keys(log(abs(12*sin(x))))

    checkbox = driver.find_element(By.ID,"robotCheckbox")
    driver.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobutton = driver.find_element(By.ID,"robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = driver.find_element(By.TAG_NAME,"button")
    driver.execute_script("return arguments[0].scrollIntoView(true);",button)
    button.click()
finally:
    time.sleep(10)
    driver.quit()