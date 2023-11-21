from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
org = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/label/span[2]')
fun = org.text
x = str(math.log(abs(12*math.sin(int(fun)))))
browser.execute_script("window.scrollBy(0, 100);")
browser.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys(x)
browser.find_element(By.ID,'robotCheckbox').click()
browser.find_element(By.ID,'robotsRule').click()
browser.find_element(By.CLASS_NAME,'btn').click()

time.sleep(10)