import psycopg2   #we need to this packge  
try: # use block 
    connection=psycopg2.connect( # connection string 
         host="localhost",
        user="postgres",
        password="121",
        dbname="postgres"
    )
    print("Connection is connected !")
except Exception as e:
    print("Connection is faild",e)