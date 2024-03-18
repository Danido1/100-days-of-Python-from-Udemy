import requests
from bs4 import BeautifulSoup
import smtplib

URL_AMAZON = "https://www.amazon.es/Russell-Hobbs-Arrocera-recipiente-antiadherente/dp/B084869TW9/ref=sr_1_5?keywords=olla%2Barrocera&qid=1677317737&sr=8-5&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
}

response = requests.get(URL_AMAZON, headers=headers)
response.raise_for_status()
webpage_data = response.text

soup = BeautifulSoup(webpage_data, "html.parser")

price = soup.find(name="span", class_="a-price-whole").getText()
clean_price = int(price.strip(","))
print(clean_price)

BUY_PRICE = 25

if clean_price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"