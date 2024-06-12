#pip install mysql-connector-python
# or
#pip3 install mysql-connector-python

import mysql.connector

#ejemplo en dominio www.freemysqlhosting.net
mydb = mysql.connector.connect(
  host="sql7.freemysqlhosting.net",
  user="sql7713450",
  password="LTBSB5K1ef"#,
  #database="mydatabase"
)

print(mydb)

#**********************************************************************
#******************** CREATE DATABASE *********************************
#**********************************************************************
database_name = "sql7713450"
"""
#no puedo hacerlo con los permisos que tengo en www.freemysqlhosting.net

database_exists = False

mycursor = mydb.cursor()

#check if database exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  if x == database_name:
    print(x)
    database_exists = True

if not database_exists:
    mycursor.execute("CREATE DATABASE " + database_name)
else:
   print("Database already exists")
"""

#me conecto a la DB
mydb = mysql.connector.connect(
  host="sql7.freemysqlhosting.net",
  user="sql7713450",
  password="LTBSB5K1ef",
  database=database_name
)

print(mydb)

#**********************************************************************
#******************** CREATE TABLE ************************************
#**********************************************************************
mycursor = mydb.cursor()

table_name = "customers"
table_exists = False

mycursor.execute("SHOW TABLES")

for x in mycursor:
  if x[0] == table_name:
     table_exists = True

#if table_exists:
#    mycursor.execute("DROP TABLE customers") # mycursor.execute("DROP TABLE IF EXISTS customers")

if not table_exists:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
else:
   print("La tabla ya existe")

#**********************************************************************
#******************** SELECT AND INSERT INTO TABLE ********************
#**********************************************************************

mycursor.execute("SELECT * FROM customers")
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2") # para paginación

myresult = mycursor.fetchall()

if len(myresult) == 0:
   print("Insertando datos de ejemplo en la tabla:")
   sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
   val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
    ]
   mycursor.executemany(sql, val) #si sólo hay una tupla, es decir, que no hay lista, se pone execute en lugar de executemay
   mydb.commit()

   print("Last RowID:", mycursor.lastrowid)

   #en caso de reciente inserción, vuelvo a hacer el Select
   mycursor.execute("SELECT * FROM customers")
   myresult = mycursor.fetchall()

print("Datos de la tabla:")
for x in myresult:
    print(f"Nombre: {x[0]}, Dirección: {x[1]}")

#**********************************************************************
#******************** UPDATE ******************************************
#**********************************************************************

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")