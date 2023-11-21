from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
browser.find_element(By.XPATH,'/html/body/div/div/div/button').click()
browser.implicitly_wait(10)

org = browser.find_element(By.XPATH, '/html/body/form/div/div/div/label/span[2]')
fun = org.text
x = str(math.log(abs(12*math.sin(int(fun)))))
browser.find_element(By.XPATH, "/html/body/form/div/div/div/input").send_keys(x)
time.sleep(1)
browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()

time.sleep(10)