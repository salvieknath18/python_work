'''
Database
'''

'''
**************************** Dataabse Connectivity with sqlite3
'''
import sqlite3

try:
    db = sqlite3.connect('pythondb')
    cursor = db.cursor()
    #cursor.execute(''' create table users (name text, email text, username text, password text, password text) ''')
    cursor.execute('''select * from users ''')
except Exception as E:
    print(E)
else:
    for row in cursor.fetchall():
        print(row)
finally:
    db.close()