from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration2.html"

driver = webdriver.Chrome()

try:
    driver.get(url)

    input1 = driver.find_element(By.CSS_SELECTOR,"div[class='first_block'] input[class='form-control first']")
    input1.send_keys("Stepan")

    time.sleep(1)

    input2 = driver.find_element(By.CSS_SELECTOR,"div[class='first_block'] input[class='form-control second']")
    input2.send_keys("Shirinkin")

    time.sleep(1)

    input3 = driver.find_element(By.CSS_SELECTOR,"div[class='first_block'] input[class='form-control third']")
    input3.send_keys("stepan_bendera@mail.ru")

    time.sleep(1)

    input4 = driver.find_element(By.TAG_NAME,"button")
    input4.click()

    time.sleep(2)

    input5 = driver.find_element(By.TAG_NAME,"h1")
    text = input5.text
    assert "Congratulations! You have successfully registered!" == text

except AssertionError:
    print("Ошибка в первом тесте")
except selenium.common.exceptions.NoSuchElementException:
    print("Ошибка во втором тесте")
finally:
    time.sleep(7)
    driver.quit()
