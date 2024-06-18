#mariodelgadopicazo
#Mx4sRHaPFHmWa6ps
#ConnectionString: mongodb+srv://mariodelgadopicazo:Mx4sRHaPFHmWa6ps@clustermdp.sgautuk.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMDP
#python -m pip install "pymongo[srv]" o ,ejor pip3 install pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://mariodelgadopicazo:Mx4sRHaPFHmWa6ps@clustermdp.sgautuk.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMDP"
# Create a new client and connect to the server
myclient = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    myclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

print(myclient.list_database_names())

#**********************************************************************
#******************** CREATE DATABASE *********************************
#**********************************************************************
database_name = "marioDB"
#no puedo hacerlo con los permisos que tengo en cloud.mongodb.com

mydb = myclient[database_name]

#**********************************************************************
#******************** CREATE COLLECTION *******************************
#**********************************************************************
#A collection in MongoDB is the same as a table in SQL databases.

print(mydb.list_collection_names()) #imprime todas las colecciones

collectionName = "readers"
mycol = mydb[collectionName] #solo con esto, se crea (o selecciona) la colección
#mycol.drop() para borrar la colección

collist = mydb.list_collection_names()
print("The collection exists.") if collectionName in collist else print("The collection is new")

#**********************************************************************
#******************** INSERT AND DELETE INTO COLLECTION **************************
#**********************************************************************
#delete one, for inserting later
myquery = { "name": "Peter" }
#myquery = { "name": { "$regex": "^P" } } #se pueden usar regular expressions
x = mycol.delete_many(myquery) #.delete_many({}) para borrar toda la tabla.

#insert one
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)

print(x.inserted_id)

#insert many
"""
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist) 

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""

#**********************************************************************
#******************** SELECT FROM COLLECTION **************************
#**********************************************************************

print('SELECT FROM COLLECTION')

x = mycol.find_one()

print(x)

#print('SELECT MANY')
#for x in mycol.find(): #es como un select *
#  print(x)

print('SELECT MANY')
myquery = { "name": "Peter" } #este es el where campo = valor
#myquery = { "address": { "$regex": "^S" } } #se pueden usar regular expressions
myselect = { "_id": False, "name": True, "address": True } #este es el select, que selecciona sólo las columnas con True (en realidad, descarta las que tengan False)
for x in mycol.find(myquery, myselect).limit(200): #.sort("name") o .sort("name", -1) para ordenar | .limit(5) para seleccionar los N primeros
  print(x)

#**********************************************************************
#******************** UPDATE FROM COLLECTION **************************
#**********************************************************************

myquery = { "name": "Richard" }
#myquery = { "name": { "$regex": "^R" } } #se pueden usar regular expressions
newvalues = { "$set": { "name": "Ricardo" } }

mycol.update_many(myquery, newvalues) #update_one para actualizar el primero que pille

print('ALL THE COLLECTION')
for x in mycol.find():
  print(x)