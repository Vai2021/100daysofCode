import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_positions = (longitude,latitude)
print(iss_positions)

