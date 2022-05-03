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
    # cursor.execute(''' create table users (name text, email text, username text, password text) ''')
    cursor.execute('''select * from person ''')
except Exception as E:
    print(E)
else:
    for row in cursor.fetchall():
        print(row)
finally:
    db.close()


conn = sqlite3.connect('example.db')

c = conn.cursor()
"""
c.execute('''
          CREATE TABLE person
          (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE address
          (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
           post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
           FOREIGN KEY(person_id) REFERENCES person(id))
          ''')

c.execute('''
          INSERT INTO person VALUES(2, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO address VALUES(2, 'python road', '1', '00000', 1)
          ''')
"""
conn.commit()
conn.close()