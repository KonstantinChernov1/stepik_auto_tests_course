from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
browser.find_element(By.XPATH, "/html/body/div/form/div/input[1]").send_keys("Roki")
browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]").send_keys("Balboa")
browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]").send_keys("kokoko@gmail.com")


current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "Gen-2 4155844328, M 5, 64f305b49dd0edoc6407.mp4"
file_path = os.path.join(current_dir, file_name)

browser.find_element(By.XPATH, "/html/body/div/form/input").send_keys(file_path)

browser.find_element(By.CLASS_NAME,'btn').click()

time.sleep(10)