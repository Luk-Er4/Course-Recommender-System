# Call cursor and db
import sqlconnector_admin
while True:
    connection, db = sqlconnector_admin.connectSQL()
    if connection == True:
        cursor = db.cursor()
        break
    else:
        print("Not responsding...")

# For sending JSON format for API
from pydantic import BaseModel
class CourseInfo(BaseModel):
    subject: str = ""
    code: str = ""
    name: str = ""

# Json formatting
from fastapi.responses import PlainTextResponse
import json

# fastapi
from fastapi import status, FastAPI, APIRouter
router = APIRouter() # course/ != course/modif/
                     # For router, do not put / at the end

#####################################################################

# Jsonify
def quryAndJsonify(query):
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return json.dumps(results, indent=4) 

# Prevent Injection / Search By Cols
def checkcolnames():
    query = '''
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = (%s)
            AND TABLE_SCHEMA = (%s)
            '''
    cursor.execute(query, ('asu_courses', 'course_recommender')) 
    return [row[0] for row in cursor.fetchall()]

# Call All Data in the Column
def checkduplicates(info):
    query = f"SELECT `{info}` FROM asu_courses"
    cursor.execute(query)
    return [row[0] for row in cursor.fetchall()]

#####################################################################

# Task 1-2: Call All Course Info (In Ordered)
@router.get("/courses/", response_class=PlainTextResponse)
def callall():
    query = '''
            SELECT * FROM asu_courses
            order by `subject`, `code`
            '''
    return quryAndJsonify(query)

@router.get("/courses/", response_class=PlainTextResponse)


# Task 3-2: Add Course Info
# MUST use JSON body for POST request
@router.post("/courses", status_code=status.HTTP_200_OK)
def addcourse(course: CourseInfo):
    query = '''
            INSERT INTO asu_courses
            (`subject`, `code`, `name`) VALUES (%s, %s, %s)
            '''
    values = (course.subject, course.code, course.name)
    cursor.execute(query, values)
    db.commit()

# Task 4-2: Modify Course Info
@router.put("/courses", status_code=status.HTTP_200_OK)
def modifcourseinfo(newdata, targetcourse, info):
    query = f'''
            UPDATE asu_courses
            set `{info}` = (%s)
            where `code` = (%s)
            '''
    values = (newdata, targetcourse)
    cursor.execute(query, values)
    db.commit()

# Task 5-2: Delete Course Info
@router.delete("/courses", status_code=status.HTTP_200_OK)
def deletecourse(code):
    query = '''
            DELETE FROM asu_courses
            WHERE `code` = (%s)
            '''
    values = (code,)
    cursor.execute(query, values)
    db.commit()

# Starter ####################################################################

app = FastAPI()

# Welcome Page
@app.get("/", status_code=status.HTTP_302_FOUND)
def welcome_message():
    results = "welsome"
    return results

app.include_router(router)

#Helpers#####################################################################

def addready(sbj, cd, nm):
    takethis = CourseInfo(subject = sbj, code = cd, name = nm)
    addcourse(takethis)

def disconnectSQL():
    cursor.close()
    db.close() 

#####################################################################

'''
@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int):
    select_query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(select_query, (user_id,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@app.post("/users", status_code=status.HTTP_201_CREATED)
def insert_user(user: DBModel):

    insert_query = """
    INSERT INTO users (username, password, email)
    VALUES (%s, %s, %s)
    """
    values = (user.username, user.email)

    try:
        cursor.execute(insert_query, values)
        mydb.commit()
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"Error: {err}")

    return {"message": "User inserted successfully"}


@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: DBModel):

    update_query = """
    UPDATE users
    SET username = %s, password = %s, email = %s
    WHERE id = %s
    """
    values = (user.username, user.email, user_id)

    cursor.execute(update_query, values)
    mydb.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}


'''

