from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
browser.find_element(By.XPATH,'/html/body/form/div/div/button').click()

alert = browser.switch_to.alert
alert.accept()

org = browser.find_element(By.XPATH, '/html/body/form/div/div/div/label/span[2]')
fun = org.text
x = str(math.log(abs(12*math.sin(int(fun)))))

browser.find_element(By.XPATH, "/html/body/form/div/div/div/inputt").send_keys(x)
browser.find_element(By.XPATH,'/html/body/form/div/div/button').click()

time.sleep(10)