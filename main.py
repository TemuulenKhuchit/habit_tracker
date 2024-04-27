import requests
from datetime import datetime

USERNAME = "temuulenkhuchit"
TOKEN = "sdf1sd56f1s65f1s6d2sdf566"

pixela_endpoint = "https://pixe.la/v1/users"

graph_id = "temuulen-graph"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": graph_id,
    "name": "Python: 100 Days of Code",
    "unit": "Qty",
    "type": "int",
    "color": "sora"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
# print(response.text)

create_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.now()
today_str: str = today.strftime("%Y%m%d")
print(today_str)

insert_data = {
    "date": today_str,
    "quantity": "3",
}

# response = requests.post(url=create_endpoint, json=insert_data, headers=graph_header)
# print(response.text)

update_endpoint = f"{create_endpoint}/{today_str}"

update_data = {
    "quantity": "3",
}

# response = requests.put(url=update_endpoint, json=update_data, headers=graph_header)
# print(response.text)

delete_endpoint = f"{create_endpoint}/{today_str}"

# response = requests.delete(url=delete_endpoint, headers=graph_header)
# print(response.text)