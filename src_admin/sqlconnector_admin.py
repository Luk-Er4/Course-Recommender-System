import mysql.connector
import bringpassword_admin

def connectSQL():
    print("connecting to SQL...")
    conn = mysql.connector

    try:
        mydb = conn.connect(
            host="localhost", 
            user="root",
            password=bringpassword_admin.pw, # ___YOUR__PASSWORD___ put your password here
            database="course_recommender" 
        )
        print("Connection to MySQL successful!")
        return mydb
    except conn.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return mydb.is_connected()
