import mysql.connector

# Establish a connection to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9322915597",
    database=" branch"
)

mycursor = mydb.cursor()

print("Connection Established")


