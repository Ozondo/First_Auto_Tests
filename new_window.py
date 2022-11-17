from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *
url = "http://suninjuly.github.io/redirect_accept.html"

driver = webdriver.Chrome()

try:
    driver.get(url)

    button1 = driver.find_element(By.TAG_NAME,"button")
    button1.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    time.sleep(1)

    x = int(driver.find_element(By.ID,"input_value").text)

    answer = driver.find_element(By.ID,"answer")
    answer.send_keys(log(abs(12*sin(x))))

    button2 = driver.find_element(By.TAG_NAME,"button")
    button2.click()

finally:
    time.sleep(6)
    driver.quit()



