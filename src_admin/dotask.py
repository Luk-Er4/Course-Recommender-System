import course_api

# Add, Modify, Deletion Must pass Through It
def injectionsafe(cursor, var):
    keywords = course_api.checkcolnames(cursor)
    return var in keywords

# Check for Duplicates for course code, course name
def CheckDuplicates(cursor, var, info):
    course_lists = course_api.checkduplicates(cursor, info)
    while True:
        return var in course_lists

# All Inputs Must Pass Here
def IsValidInput(cursor, info):
    while True:
        var = input(f"What is {info}? Type: ")
        # Checks future risk for SQL Injection
        if injectionsafe(cursor, var):
            print("Invalid input name!")
            continue
        # (Extra Step for "code" & "name") Check Duplicates
        if info in ["code", "name"]:
            if CheckDuplicates(cursor, var, info):
                print(f"There is a duplicated {var} in {info}")
                continue         
        return var

# Task 1-1
def GetAllCourse(cursor):
    print("Show All Course Info")
    print(course_api.callall(cursor))

# Task 2-1
def SearchBy(cursor):
    return ""

# Task 3-1
def AddCourse(cursor, db):
    sbj  = IsValidInput(cursor, "subject")
    code = IsValidInput(cursor, "code")
    name = IsValidInput(cursor, "name")
    course_api.addcourse(cursor, db, sbj, code, name) 
    print("perfect!")

# Task 4-1
def ModifyCourse(cursor):
    return ""

# Task 5-1
def DeleteCourse(cursor, db):
    code = IsValidInput(cursor, "course code to delete?")
    # Check the typed course is in the "code" column
    if CheckDuplicates(cursor, code, "code"):
        course_api.deletecourse(cursor, db, code)
        print(f"course {code} has been deleted!")
    else:
        print("Nothing to delete...")
    

