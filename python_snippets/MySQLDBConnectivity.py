'''
Database
'''

'''
**************************** Dataabse Connectivity with MySQL
'''

try:
    # Open database connection
    db = pymysql.connect("localhost", "eknath", "1nath@Mysql", "test")

    # prepare a cursor object using cursor() method
    query = db.cursor()

    # execute SQL query using execute() method.
    data = query.execute("select * from student_info")

    # Fetch a single row using fetchone() method.
    data = query.fetchone()
    print("Database version : %s " % data)

except Exception as E :
    print(E)

finally:
    # disconnect from server
    db.close()

'''
**************************** Databse Connectivity with Sqlite3
'''
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()
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
          INSERT INTO person VALUES(1, 'pythoncentral')
          ''')
c.execute('''
          INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
          ''')

conn.commit()
conn.close()