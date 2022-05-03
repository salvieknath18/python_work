import json
'''
student_data = {
    1: {'name': 'ABCD', 'subject': ['Math', 'English']},
    2: {'name': 'XYZ', 'subject': ['Math2', 'English']},
    3: {'name': 'PQR', 'subject': ['Math', 'English2']}
}
json.dump(student_data, open("sample_test.json", 'w'))
'''

student_data = json.load(open("sample_test.json"))

for k, v in student_data.items():
    for key, val in v.items():
        print(key, ": ", val)
#print(student_data)












