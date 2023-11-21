import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
org = browser.find_element(By.ID, 'treasure')
x = org.get_attribute("valuex")
fun = str(math.log(abs(12*math.sin(int(x)))))
browser.find_element(By.ID, "answer").send_keys(fun)
browser.find_element(By.ID,'robotCheckbox').click()
browser.find_element(By.ID,'robotsRule').click()
browser.find_element(By.CLASS_NAME,'btn').click()

time.sleep(20)

browser.quit()