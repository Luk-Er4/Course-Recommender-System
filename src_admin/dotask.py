import course_api

# Add, Modify, Deletion Must pass Through It
def IsColName(cursor, var):
    keywords = course_api.checkcolnames(cursor)
    return var in keywords

# Check for Duplicates for course code, course name
def CheckDuplicates(cursor, var, info):
    course_lists = course_api.checkduplicates(cursor, info)
    while True:
        return var in course_lists

# Check all the input chars are alphnum
def CheckValidChars(var, info):
    # Other than subject, name, code, Space is not allowed
    spacecount = 0
    if info in ["subject", "name", "topic"]:
        spacecount = 6

    for c in var:
        if c.isalnum():
            continue
        if c.isspace(): 
            spacecount = spacecount - 1
            if spacecount < 0:
                print("Too much spaces are used for this feature")
                return False
            continue
        else: 
            print("Must be alphabet, numbers, or space (in need)")
            return False
    return True

# All Inputs Must Pass Here
def IsValidInput(cursor, info, checkDup = "Y"):
    while True:
        var = input(f"What is {info}? Type: ")
        # Checks all chars are alphnum
        if CheckValidChars(var, info): pass
        else: continue
        # Checks future risk for SQL Injection
        if IsColName(cursor, var):
            print("Avoid using those names!")
            continue
        # (Extra Step for "code" & "name") Check Duplicates
        if info in ["code", "name"] and checkDup == "Y":
            if CheckDuplicates(cursor, var, info):
                print(f"There is a duplicated {var} in {info}")
                continue         
        return var
    
########################################################################

# Task 1-1
def GetAllCourse(cursor):
    print("Showing All Course Info...")
    print(course_api.callall(cursor))

# Task 2-1
def SearchBy(cursor):
    keywords = course_api.checkcolnames(cursor)

    return ""

# Task 3-1
def AddCourse(cursor, db):
    sbj  = IsValidInput(cursor, "subject")
    code = IsValidInput(cursor, "code")
    name = IsValidInput(cursor, "name")
    course_api.addcourse(cursor, db, sbj, code, name) 
    print("perfect!")

# Task 4-1
def ModifyCourse(cursor, db):
    # Modify course info based on course code
    print("Type the course code to modify information")
    code = IsValidInput(cursor, "code", "N")
    if CheckDuplicates(cursor, code, "code"):
        # But first, ask if the user need to change course code
        decision = input("Before modify the course info, Do you have to change the code? Y/N: ")
        if decision == 'Y':
            print("Type the new course code: ")
            newcode = IsValidInput(cursor, "code")
            if CheckDuplicates(cursor, newcode, "code"):
                print(f"{newcode} already exists!" )
            else:
                course_api.modifcourseinfo(cursor, db, newcode, code, "code")
                code = newcode
        # Then change something
        print("What do you want to change? Here are the list: ")
        print(course_api.checkcolnames(cursor))
        col = input("Choose One: ")
        if IsColName(cursor, col):
            print("Set new data: ")
            new = IsValidInput(cursor, col)
            course_api.modifcourseinfo(cursor, db, new, code, col)
        else:
            print("Invalid input... Terminate")
    else:
        print(f"There is no {code} in database. Terminate.")
    
    return ""

# Task 5-1
def DeleteCourse(cursor, db):
    code = IsValidInput(cursor, "course code to delete?")
    # Check the existing course is in the "code" column
    if CheckDuplicates(cursor, code, "code"):
        course_api.deletecourse(cursor, db, code)
        print(f"course {code} has been deleted!")
    else:
        print("Nothing to delete...")

# Last Thing
def MakeOrdered(cursor, db):
    course_api.makeordered(cursor, db)
