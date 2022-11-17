from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
url = "http://suninjuly.github.io/file_input.html"

driver = webdriver.Chrome()

try:
    driver.get(url)

    first_name = driver.find_element(By.NAME,"firstname")
    first_name.send_keys("Ivan")


    last_name = driver.find_element(By.NAME,"lastname")
    last_name.send_keys("Ivanov")


    email = driver.find_element(By.NAME,"email")
    email.send_keys("Ivanov@mail.ru")


    file = driver.find_element(By.ID,"file")
    current_dir = os.path.abspath(os.path.dirname("txt.txt")) #Ищем текущую директорию, где лежит файл
    file_path = os.path.join(current_dir, 'txt.txt') #добавляем к этому пути имя файла
    file.send_keys(file_path)

    but = driver.find_element(By.TAG_NAME,"button")
    but.click()
finally:
    time.sleep(5)
    driver.quit()
