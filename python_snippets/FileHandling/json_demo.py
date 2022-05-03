import json

data = {1: "one", 'l1':[1,2,3]}
print(data['l1'])
jdata = json.dumps(data)
print(jdata['l1'])
