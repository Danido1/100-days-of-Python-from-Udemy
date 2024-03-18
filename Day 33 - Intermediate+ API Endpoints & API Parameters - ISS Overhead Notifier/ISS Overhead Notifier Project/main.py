import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.39672034899821 # Your latitude
MY_LONG = -3.608298616185555 # Your longitude

def is_iss_overhead()
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    #Your position is within +5 or -5 degrees of the ISS position.

    if 35 <= iss_latitude <= 45 and -8 <= iss_longitude <= 2:
        return True
def is_dark()
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise, sunset)

    time_now = datetime.now()

    if sunrise >= time_now >= sunset:
        #It is dark
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.ethereal.email", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Works Now!\n\n {random_quote}".encode("utf8"))





