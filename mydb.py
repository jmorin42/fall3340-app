import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password',
)

# Prepare cursor object (using the connector declared above)
cursorObject = dataBase.cursor() 

# Create database
cursorObject.execute("CREATE DATABASE todoDB")

# Message in console to see if it worked 
print("todoDB created successfully!")