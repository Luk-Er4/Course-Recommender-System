# fastapi
from fastapi import status, FastAPI

# Json formatting
from fastapi.responses import PlainTextResponse
import json

# start app
app = FastAPI()

def quryAndJsonify(query, cursor):
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return json.dumps(results, indent=4) 

@app.get("/", status_code=status.HTTP_302_FOUND)
def welcome_message():
    results = "welsome"
    return results

@app.get("/subject", response_class=PlainTextResponse)
def searchby(cursor):
    query = "SELECT * FROM asu_courses"
    return quryAndJsonify(query, cursor)

