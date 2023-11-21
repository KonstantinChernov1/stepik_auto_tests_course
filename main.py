from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
# link1 = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
# link1.click()
input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
input2.send_keys("Petrov")
input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[3]/input")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[4]/input")
input4.send_keys("Russia")
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()