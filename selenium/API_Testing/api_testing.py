import requests
import json
import jsonpath

response = requests.get(r"https://reqres.in/api/users?page=2")
print(response.status_code)
# response = requests.delete(r"https://reqres.in/api/users/2")

print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))
print("******************************************************************")
print(response.cookies)
print("******************************************************************")
print(response.elapsed)
print("******************************************************************")
print(response.text)
print("******************************************************************")
print(response.status_code)
print("******************************************************************")
print(response.content)


assert response.status_code == 200
pdata = json.loads(response.text)
pages = jsonpath.jsonpath(pdata,'total_pages')
assert pages[0]==2


pdata = {
    "name": "morpheus",
    "job": "leader"
}
jdata = json.dumps(pdata)
response = requests.post(r"https://reqres.in/api/users", jdata)
print(response.status_code)
assert response.status_code == 201