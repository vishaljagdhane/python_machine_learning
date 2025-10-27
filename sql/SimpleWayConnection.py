# print("Create Simple dataBase connection ")
import psycopg2

databaseconnection= psycopg2.connect(
       host="localhost",
        user="postgres",
        password="121",
        dbname="postgres"
)
if databaseconnection:
    print("Welcome to the database connection")
else:
    print("Some went worng")
