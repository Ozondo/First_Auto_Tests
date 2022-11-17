import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

url = "https://suninjuly.github.io/selects2.html"

try:
    driver.get(url)

    num1 = driver.find_element(By.ID,"num1").text
    num1 = int(num1)

    num2 = driver.find_element(By.ID,"num2").text
    num2 = int(num2)

    summ = str(num1+num2)

    select = Select(driver.find_element(By.ID,"dropdown"))
    select.select_by_value(summ)


    but = driver.find_element(By.TAG_NAME,"button")
    but.click()

finally:
    time.sleep(2)
    driver.quit()