import sqlite3

file = open("emp_data.txt", "r")
#content = file.readlines()
emp_list = list()
key = ['name', 'age', 'cName', 'salary', 'designation']
for line in file.readlines():
    dlist =  line.strip().split()
    d = dict()
    for i in range(len(dlist)):
        d[key[i]] = dlist[i]
    emp_list.append(d)
file.close()
print(emp_list)

db = sqlite3.connect('pythondb1')
cursor = db.cursor()
"""
cursor.execute(''' CREATE TABLE user1(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   CNAME          TEXT    NOT NULL,
   SALARY         REAL,
   DESIGNATION          TEXT    NOT NULL
);''')"""
"""
for i, user in enumerate(emp_list):
    cursor.execute(f"INSERT INTO user1 VALUES ({i+1}, '{user['name']}', '{user['cName']}', {user['salary']},  '{user['designation']}');")
db.commit()
"""
query = "select * from user1 where cname='Google'"
cursor.execute(query)
result = cursor.fetchall()
db.commit()
print(result)
db.commit()
db.close()