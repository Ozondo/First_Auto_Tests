import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from math import *

url = "https://suninjuly.github.io/math.html"

driver = webdriver.Chrome()

try:
    driver.get(url)
    number = driver.find_element(By.ID,"input_value")
    number = int(number.text)

    answer = driver.find_element(By.ID,"answer")
    answer.send_keys(log(abs(12*sin(number))))

    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    raddiobutton = driver.find_element(By.ID,"robotsRule")
    raddiobutton.click()
    time.sleep(2)
    button = driver.find_element(By.TAG_NAME,"button")
    button.click()
finally:
    time.sleep(5)
    driver.quit()
