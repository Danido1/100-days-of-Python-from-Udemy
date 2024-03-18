from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVE_PATH = r"C:\Users\Daniel\Desktop\Development\chromedriver.exe"


promised_down = 500
promised_up = 500
internet_speed_url = "https://www.speedtest.net/es/result/14553402098"



class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(CHROME_DRIVE_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(internet_speed_url)
        self.driver.maximize_window()
        button_cokies = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]")
        time.sleep(5)
        button_cokies.click()
        button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").get_attribute("textContent")
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").get_attribute("textContent")
        print(self.up, self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        self.driver.maximize_window()

        time.sleep(10)
        email = self.driver.find_element(By.XPATH,
                    "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input")
        email.send_keys("dadoru95@gmail.com")
        time.sleep(10)
        next_button = self.driver.find_element(By.XPATH,
                                           "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div")
        next_button.click()
        password = self.driver.find_element(By.XPATH,
            "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input")

        password.send_keys("carivetillo08")
        time.sleep(10)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        tweet_compose = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(10)

        tweet_button = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(10)
        self.driver.quit()


hello = InternetSpeedTwitterBot()

hello.get_internet_speed()
hello.tweet_at_provider()



