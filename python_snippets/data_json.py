import json

data2 = [{'name':'ABC','age':50,'PNo.':'9876543210'},
         {'name':'PQR','age':20,'PNo.':'9876543210'},
         {'name':'AMV','age':25,'PNo.':'9876543210'},
         {'name':'XYZ','age':35,'PNo.':'9876543210'},
         {'name':'RVT','age':40,'PNo.':'9876543210'}]

with open("data.json",'w') as f:
    f.write(json.dumps(data2))
json.dump(data2, open("data1.json"))

data3 = json.load(open('data.json'))
data4 = json.loads(json.dumps(data2))
print(data3)
