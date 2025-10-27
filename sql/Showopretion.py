print("Check connection and database")
import psycopg2

try:
    # Connect to PostgreSQL
    databaseConnection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="121",
        dbname="postgres"  # ✅ Required
    )
    print("✅ Database is successfully connected")

    myCursor = databaseConnection.cursor()
    myCursor.execute("SELECT datname FROM pg_database;")  # ✅ PostgreSQL query

    print("📋 Databases:")
    for x in myCursor:
        print("-", x[0])

except Exception as e:
    print("❌ Connection failed:", e)

finally:
    if 'myCursor' in locals():
        myCursor.close()
    if 'databaseConnection' in locals():
        databaseConnection.close()
        print("🔒 Connection closed")
