import psycopg2
datbase_connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="122"
)

if datbase_connection :
 print("This the database connnection sucessfullyconnected",datbase_connection)
else:
 print("Data Base is not connected to system ")