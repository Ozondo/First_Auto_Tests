from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

url = "http://suninjuly.github.io/alert_accept.html"

driver = webdriver.Chrome()

try:
    driver.get(url)

    button = driver.find_element(By.TAG_NAME,"button")
    button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    time.sleep(1)

    x = int(driver.find_element(By.ID,"input_value").text)

    answer = driver.find_element(By.ID,"answer")
    answer.send_keys(log(abs(12*sin(x))))

    button2 = driver.find_element(By.TAG_NAME,"button")
    button2.click()


finally:
    time.sleep(5)
    driver.quit()