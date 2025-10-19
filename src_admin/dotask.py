import course_api

# Add, Modify, Deletion Must pass Through It
def IsColName(var):
    keywords = course_api.checkcolnames()
    return var in keywords

# Check for Duplicates for course code, course name
def CheckDuplicates(var, info):
    course_lists = course_api.checkduplicates(info)
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
def IsValidInput(info, checkDup = "Y"):
    while True:
        var = input(f"What is {info}? Type: ")
        # Checks all chars ar e alphnum
        if CheckValidChars(var, info): pass
        else: continue
        # Checks future risk for SQL Injection
        if IsColName(var):
            print("Avoid using those names!")
            continue
        # (Extra Step for "code" & "name") Check Duplicates
        if info in ["code", "name"] and checkDup == "Y":
            if CheckDuplicates(var, info):
                print(f"There is a duplicated {var} in {info}")
                continue         
        return var
    
########################################################################

# Task 1-1
def GetAllCourse():
    print("Showing All Course Info...")
    print(course_api.callall())

# Task 2-1
def SearchBy():
    print("You can search courses by [1. ]")

    return ""

# Task 3-1
def AddCourse():
    sbj  = IsValidInput("subject")
    cd = IsValidInput("code")
    nm = IsValidInput("name")
    course_api.addready(sbj, cd, nm) 
    print("perfect!")

# Task 4-1
def ModifyCourse():
    # Modify course info based on course code
    print("Type the course code to modify information")
    code = IsValidInput("code", "N")
    if CheckDuplicates(code, "code"):
        # But first, ask if the user need to change course code
        decision = input("Before modify the course info, Do you have to change the code? Y/N: ")
        if decision == 'Y':
            print("Type the new course code: ")
            newcode = IsValidInput("code")
            if CheckDuplicates(newcode, "code"):
                print(f"{newcode} already exists!" )
            else:
                course_api.modifcourseinfo(newcode, code, "code")
                code = newcode
        # Then change something
        print("What do you want to change? Here are the list: ")
        lists = course_api.checkcolnames()
        lists.remove('code')
        print(lists)
        col = input("Choose One: ")
        if col in lists:
            print("Set new data: ")
            new = IsValidInput(col)
            course_api.modifcourseinfo(new, code, col)
        else:
            print("Invalid input... Terminate")
    else:
        print(f"There is no {code} in database. Terminate.")

# Task 5-1
def DeleteCourse():
    code = IsValidInput("course code to delete?")
    # Check the existing course is in the "code" column
    if CheckDuplicates(code, "code"):
        course_api.deletecourse(code)
        print(f"course {code} has been deleted!")
    else:
        print("Nothing to delete...")

# Finish Task
def FinishTask():
    course_api.disconnectSQL()
