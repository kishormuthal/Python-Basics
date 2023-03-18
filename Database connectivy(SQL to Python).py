# In this we learn SQL Database connectivity with Python
 
# import the mysql connector
import mysql.connector

# create a connection bw mysql and python(vs code)
mydb1 = mysql.connector.connect( 
  host = "localhost",
  user = "abc",
  password = "password"
)

# print the connection
print(mydb1)

#create a cursor to perform opertion in mysql by python
mycursor = mydb1.cursor()

# now with the help of this cursor we can perform any operation in mysql by python
# OPERATION = show all databases present in current directory
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

#OPERATION = create a database
mycursor.execute("CREATE DATABASE IF NOT EXISTS TEST1DB")

#OPERATION = create a Table inside a  database
mycursor.execute("CREATE TABLE IF NOT EXISTS TEST1DB.test_table1(c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(100))")

#OPERATION = Insert a value in a table
mycursor.execute("INSERT INTO TEST1DB.test_table1 VALUE(10,'kishor',45, 10.45,'muthal')")
mydb1.commit()

#OPERATION = Read a value from a table
mycursor.execute("SELECT * FROM TEST1DB.test_table1")
for x in mycursor.fetchall():
  print(x)


