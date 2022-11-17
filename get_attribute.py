import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from math import *

url = "http://suninjuly.github.io/get_attribute.html"

driver = webdriver.Chrome()

try:
    driver.get(url)
    picture = driver.find_element(By.TAG_NAME,"img")
    number = int(picture.get_attribute("valuex"))

    answer = driver.find_element(By.ID,"answer")
    answer.send_keys(log(abs(12*sin(number))))

    checkbox = driver.find_element(By.ID,"robotCheckbox")
    checkbox.click()

    radiobutton = driver.find_element(By.ID,"robotsRule")
    radiobutton.click()

    time.sleep(2)

    submit = driver.find_element(By.TAG_NAME,"button")
    submit.click()

finally:
    time.sleep(5)
    driver.quit()
