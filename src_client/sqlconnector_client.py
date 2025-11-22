import mysql.connector
import bringpassword_client

def connectSQL():
    print("connecting to SQL...")
    conn = mysql.connector
    connection_status = False

    try:
        mydb = conn.connect(
            host=bringpassword_client.db_endpoint, 
            user="user",
            password=bringpassword_client.pw, # ___YOUR__PASSWORD___ put your password here
            database="course_recommender" 
        )
        print("Connection to MySQL successful!")
    except conn.Error as err:
        print(f"Error connecting to MySQL: {err}")

    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM asu_courses order by subject")
        results = cursor.fetchall()  # Fetch all rows

        connection_status = True

        mydb.close()

    rows_num, cols_num = len(results), len(results[0])
    print(rows_num, "courses", cols_num, "data per each course")

    return connection_status, results
