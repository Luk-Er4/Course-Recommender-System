import mysql.connector

def connectSQL():
    print("connecting to SQL...")
    conn = mysql.connector

    try:
        mydb = conn.connect(
            host="localhost", 
            user="root",
            password="___YOUR__PASSWORD___", # put your password here
            database="course_recommender" 
        )
        print("Connection to MySQL successful!")
    except conn.Error as err:
        print(f"Error connecting to MySQL: {err}")

    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM asu_courses order by 'subject' and code")
        results = cursor.fetchall()  # Fetch all rows

        mydb.close()

    rows_num, cols_num = len(results), len(results[0])
    print(rows_num, "courses", cols_num, "data per each course")

    return results