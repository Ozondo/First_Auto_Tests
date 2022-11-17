from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/find_link_text"

driver = webdriver.Chrome()

try:
    driver.get(link)
    ssilka = driver.find_element(By.LINK_TEXT,str(math.ceil(math.pow(math.pi, math.e)*10000)))
    time.sleep(2)
    ssilka.click()
finally:
    time.sleep(10)
    driver.quit()