import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchT" \
      "erm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22" \
      "south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterStat" \
      "e%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22va" \
      "lue%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%" \
      "3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2" \
      "C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A87262" \
      "7%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

url_forms = "https://docs.google.com/forms/d/e/1FAIpQLSc6Bfr3pJrsazZ1fkSCA1mXEEksAHumS8B38ZgR6scsOrxv5w/viewform"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
}


response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")


data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
    .contents[0]
    .strip("!<>-")
)

# Get houses links

house_links = [
    result["detailUrl"]
     for result in data["cat1"]["searchResults"]["listResults"]
    ]

# amend house_links to have all proper URLS
house_links = [
    link.replace(link, "https://www.zillow.com" + link)
    if not link.startswith("http")
    else link
    for link in house_links
]

# Get address
house_address = [
    result["address"]
    for result in data["cat1"]["searchResults"]["listResults"]
]

# Get price
house_rent = [
    int(result["units"][0]["price"].strip("$").replace(",", "").strip("+"))
    if "units" in result
    else result["unformattedPrice"]
    for result in data["cat1"]["searchResults"]["listResults"]
]

CHROME_DRIVE_PATH = r"C:\Users\Daniel\Desktop\Development\chromedriver.exe"

class Google_Forms:
    def __init__(self):
        self.service = Service(CHROME_DRIVE_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        time.sleep(5)

    def add_data(self):
        self.driver.get(url_forms)
        self.driver.maximize_window()
        for i in range(len(house_address)):
            add_address = self.driver.find_element(By.XPATH,
                                                   "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            add_rent = self.driver.find_element(By.XPATH,
                                                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")

            add_links = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            add_address.send_keys(house_address[i])
            add_rent.send_keys(house_rent[i])
            add_links.send_keys(house_links[i])
            send_button = self.driver.find_element(By.XPATH,
                                        "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
            send_button.click()
            time.sleep(5)
            send_another_response = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            send_another_response.click()
            time.sleep(5)

hello = Google_Forms()

hello.add_data()





