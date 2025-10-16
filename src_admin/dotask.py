import course_api

def injectionsafe(cursor, info):
    keywords = course_api.checkcolnames(cursor)
    var = input(f"What is {info}? Type: ")
    while var in keywords:
        print(var, "is NOT allowed name. Type: ")
        var = input(f"What is {info}? Type: ")
    return var

def GetAllCourse(cursor):
    print("Show All Course Info")
    print(course_api.callall(cursor))
    
def SearchBy(cursor):
    print(course_api.checkcolnames(cursor))
    return ""

def AddCourse(cursor, db):
    sbj  = injectionsafe(cursor, "subject")
    code = injectionsafe(cursor, "course code")
    name = injectionsafe(cursor, "course name")
    course_api.addcourse(cursor, db, sbj, code, name) 
    print("perfect!")

def ModifyCourse(cursor):
    return ""

def DeleteCourse(cursor, db):
    code = injectionsafe(cursor, "course name to delete?")
    course_api.deletecourse(cursor, db, code)
    print("perfect!")

