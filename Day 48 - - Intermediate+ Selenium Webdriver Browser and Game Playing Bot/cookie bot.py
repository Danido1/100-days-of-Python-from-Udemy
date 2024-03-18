from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\Daniel\Desktop\Development\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Cookie
cookie_click = driver.find_element(By.ID, "cookie")

# Items to buy
items = driver.find_elements(By.ID, "store")
item_ids = [item.get_attribute("id") for item in items]

# cookie count
cookies = int(driver.find_element(By.ID, "money").text.replace(",", ""))
while True:
    for i in range(0, 500):
        cookie_click.click()

    for i in range(0, 5):
        prices = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for i in range(len(prices), -1, -1):
            try:
                prices[i].click()
            except:
                continue

    if time.time() > time.time() + 60 * 5:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break









