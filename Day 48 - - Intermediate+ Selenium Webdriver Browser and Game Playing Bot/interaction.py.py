from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\Daniel\Desktop\Development\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://app.usertesting.com/users/sign_in")

# number_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# number_of_articles.click()

email = driver.find_element(By.NAME, "email")
email.send_keys("test@hotmail.com")


password = driver.find_element(By.NAME, "password")
password.send_keys("123456")

log_in = driver.find_element(By.CSS_SELECTOR, ".form-group")
log_in.click()




