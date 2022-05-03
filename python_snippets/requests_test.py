import requests
import json

response = requests.get(r"https://reqres.in/api/users?page=2")
# print(response.status_code)
pdata = json.loads(response.text)
print(pdata)
