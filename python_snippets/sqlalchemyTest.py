import sqlalchemy as db
import pandas as pd
engine = db.create_engine('mysql+pymysql://eknath:1nath@Mysql@localhost/classicmodels')
connection = engine.connect()
metadata = db.MetaData()
customers = db.Table('customers', metadata, autoload=True, autoload_with=engine)
offices = db.Table('offices', metadata, autoload=True, autoload_with=engine)
products = db.Table('products', metadata, autoload=True, autoload_with=engine)
productlines = db.Table('productlines', metadata, autoload=True, autoload_with=engine)

# equivalent to :- Select * from customers
Q = db.select([customers])
ResultProxy = connection.execute(Q)  # Returns Object for above query
ResultSet1 = ResultProxy.fetchall()  # Returns all the data in the form of list for above query

ResultSet11 = connection.execute(db.select([customers])).fetchall()  # Select all data
ResultSet12 = connection.execute(db.select([customers])).fetchmany(3) # Select first 3 data or
ResultSet13 = ResultSet11[:3]

# equivalent to :- SELECT * FROM customers WHERE customerName = 'Atelier graphique'
Q = db.select([customers]).where(customers.columns.customerName == 'Atelier graphique')  # Filter by column value
ResultSet2 = connection.execute(Q).fetchall()

# equivalent to :- SELECT phone, country FROM offices WHERE city IN ('NYC', 'paris')
Q = db.select([offices.columns.phone, offices.columns.country]).where(offices.columns.city.in_(['NYC','paris']))
ResultSet3 = connection.execute(Q).fetchall()

# equivalent to :- SQL :SELECT phone, city FROM offices WHERE country = 'USA' AND NOT city = 'NYC'
Q = db.select([offices.columns.phone, offices.columns.city]).where(db.and_(offices.columns.country == 'USA', offices.columns.city != 'NYC'))
ResultSet4 = connection.execute(Q).fetchall()
'''similarly for or, and, not'''

# equivalent to :- SELECT * FROM offices ORDER BY country DESC, city
Q = db.select([offices]).order_by(db.desc(offices.columns.country),offices.columns.city)
ResultSet5 = connection.execute(Q).fetchall()
df = pd.DataFrame(ResultSet5)
df.columns = ResultSet5[0].keys()
df.head(5)


# equivalent to :- SELECT SUM(buyPrice) from products
Q = db.select([db.func.sum(products.columns.buyPrice)])
ResultSet6 = connection.execute(Q).fetchall()
'''Similarly avg(), count(), min(), max() functions can be use'''

# equivalent to :- SELECT SUM(buyPrice) as buyPrice, productLine FROM products GROUP BY productLine
Q = db.select([db.func.sum(products.columns.buyPrice), products.columns.productLine]).group_by(products.columns.productLine)
ResultSet7 = connection.execute(Q).fetchall()

# equivalent to :- SELECT DISTINCT productLine FROM products
Q = db.select([products.columns.productLine.distinct()])
ResultSet8 = connection.execute(Q).fetchall()

'''
The case() expression accepts a list of conditions to match and the column to return 
if the condition matches, followed by an else_ if none of the conditions match.
cast() function to convert an expression to a particular type
We use .scalar to the result when the result contains only single value
eg. to calculate percentage buyPrice for motorcycles wrt total buyPrice
'''
# equivalent to :- SELECT SUM(buyPrice) as buyPrice FROM products where productLine='Motorcycles'
motorcycles_buyPrice_query = db.func.sum(db.case([(products.columns.productLine == 'Motorcycles', products.columns.buyPrice)],else_=0))
ResultSet9 = connection.execute(motorcycles_buyPrice_query).fetchall()
total_buyPrice_query = db.cast(db.func.sum(products.columns.buyPrice), db.DECIMAL)
final_percentage_query = db.select([motorcycles_buyPrice_query/total_buyPrice_query * 100])
ResultSet10 = connection.execute(final_percentage_query).scalar()

# equivalent to :- Joins two tables automatic(Here products=110 and productlines=7, so join gives 770 Records)
Q = db.select([products, productlines])
#Q = db.select([products.columns.productLine, productlines.columns.productLine]) # check for only two column
ResultSet11 = connection.execute(Q).fetchall()

select_ResColumns_query = db.select([products, productlines])
#select_ResColumns_query = db.select([products.columns.productLine, productlines.columns.productLine]) # check for only two column
Q = select_ResColumns_query.select_from(products.join(productlines, products.columns.productLine == productlines.columns.productLine))
ResultSet12 = connection.execute(Q).fetchmany(3)
print(len(ResultSet12))
print(ResultSet12)

'''*******************            To Create Table
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
'''

''' *****************     Insert Into Table
#Inserting record one by one
query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True) 
ResultProxy = connection.execute(query)

#Inserting many records at ones
query = db.insert(emp) 
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)
'''

'''  ****************      Updating Data in Table
db.update(table_name).values(attribute = new_value).where(condition)
# Build a statement to update the salary to 100000
query = db.update(emp).values(salary = 100000).where(emp.columns.Id == 1)
results = connection.execute(query)
'''

''' ****************       Deleting data from Table
db.delete(table_name).where(condition)
# Build a statement to delete where salary < 100000
query = db.delete(emp).where(emp.columns.salary < 100000)
results = connection.execute(query)
'''

''' ***************          Drop tables
table_name.drop(engine) #drops a single table
metadata.drop_all(engine) #drops all the tables in the database
'''