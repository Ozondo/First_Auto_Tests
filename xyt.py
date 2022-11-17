import time
from math import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

url = "http://suninjuly.github.io/explicit_wait2.html"

driver=webdriver.Chrome()

try:
    driver.get(url)

    price = WebDriverWait(driver,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))

    button = driver.find_element(By.TAG_NAME,"button")

    button.click()



    x = int(driver.find_element(By.ID,"input_value").text)

    answer = driver.find_element(By.ID,"answer")
    answer.send_keys(log(abs(12*sin(x))))

    button2 = driver.find_element(By.ID,"solve")
    button2.click()


finally:
    time.sleep(20)
    driver.quit()
