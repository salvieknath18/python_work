import sqlalchemy as db
engine = db.create_engine('sqlite:///test.sqlite') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()
emp = db.Table('emp', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )
metadata.create_all(engine) #Creates the table

query = db.insert(emp).values(Id=10, name='ABCD', salary=60000.00, active=True)
ResultProxy = connection.execute(query)

Q = db.select([emp])
ResultSet1 = connection.execute(Q).fetchall()
print(ResultSet1)