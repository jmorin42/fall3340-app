import mysql.connector
from decouple import config

dataBase = mysql.connector.connect(
	host = config('MYSQL_HOST'),
	user = config('MYSQL_USER'),
	passwd = config('MYSQL_PASSWORD'),
)

# Prepare cursor object (using the connector declared above)
cursorObject = dataBase.cursor() 

# Create database
cursorObject.execute("CREATE DATABASE todoDB")

# Message in console to see if it worked 
print("todoDB created successfully!")