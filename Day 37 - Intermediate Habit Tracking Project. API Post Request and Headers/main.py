import requests
from datetime import datetime

date_to_update = datetime(year=2023, month=1, day=15)

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = "https://pixe.la/v1/users/danido/graphs"
MY_GRAPH_ID = "https://pixe.la/v1/users/danido/graphs/graph1"
UPDATE_ENDPOINT = "https://pixe.la/v1/users/danido/graphs/graph1/20230116"


# My pixela account
USERNAME = "danido"
TOKEN = "mypixelapassword12345"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
 ## Create account at pixela
#r = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(r.text)

# Create graph
graph_config = {
    "id": "graph1",
    "name": "swimming",
    "unit": "km",
    "type": "float",
    "color": "sora"

}

headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.now()

#r = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
#print(r.text)

# Fill one pixel of the graph
graph1_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many km did you swim today?"),
}

r = requests.post(url=MY_GRAPH_ID, json=graph1_params, headers=headers)
print(r.text)

#print(today.strftime("%Y%m%d"))
new_graph1_params = {
    "quantity": "10.0"
}
# UPDATE PIXEL FROM GRAPH1
#r = requests.put(url=UPDATE_ENDPOINT, json=new_graph1_params, headers=headers)
#print(r.text)

# DELETE A PIXEL GROM GRAPH1

#r = requests.delete(url=UPDATE_ENDPOINT, headers=headers)
#print(r.text)