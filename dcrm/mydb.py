import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

#prepare cursor object
cursorObject = database.cursor()

#Create a database 
cursorObject.execute("CREATE DATABASE db")

print("All done! Database created")