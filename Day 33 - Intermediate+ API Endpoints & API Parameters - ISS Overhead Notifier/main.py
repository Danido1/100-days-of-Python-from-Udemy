import requests
from datetime import datetime

MY_LAT = 40.39672034899821
MY_LNG = -3.608298616185555

#response = requests.get(url="http://api.open-notify.org/iss-now.json")

#if response.status_code == 404:
    #raise Exception("That resource does not exist")
#elif response.status_code == 401:
    #print("You are not authorised to acess this data.

# Instead of trying to raise an exception for every single possible status code and telling the developer what might be
# reason, we can simply use the request module by sayin:

#response.raise_for_status()
#data = response.json()

#longitude = data["iss_position"]["longitude"]
#latitude = data["iss_position"]["latitude"]

#iss_position = (longitude, latitude)
#print(iss_position)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,

}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)