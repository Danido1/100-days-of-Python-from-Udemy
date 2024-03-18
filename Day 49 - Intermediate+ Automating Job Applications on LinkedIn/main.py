import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os

user = os.environ.get("USER")
password = os.environ.get("PASSWORD")

chrome_driver = r"C:\Users\Daniel\Desktop\Development\chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

url_job = "https://www.linkedin.com/jobs/view/3496216323/?eBP=CwEAAAGHB9GFMY3lFmqgmBU1rBtnS-_k4zzq952DRSdklOewqQFxSwGe"
url_login = "https://es.linkedin.com/"

driver.get(url_login)



# login
user_element = driver.find_element(By.ID, "session_key")
password_element = driver.find_element(By.ID, "session_password")

user_element.send_keys(user)
password_element.send_keys(password)
password_element.send_keys(Keys.ENTER)



# job application
time.sleep(2)
driver.get(url_job)
driver.maximize_window()
time.sleep(2)
apply = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[3]/div/div/div/button")
apply.click()
time.sleep(2)
next = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
next.click()
time.sleep(5)
next.click()
time.sleep(5)




