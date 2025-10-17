# Start
print("This is Admin software for accessing course data.")

# Initialize the software for admin
import sqlconnector_admin

while True:
    connection, db = sqlconnector_admin.connectSQL()
    if connection == True:
        _db = db
        cursor = db.cursor()
        break

# Entered Admin / Choose Tasks 
print("You have an authority to \n 1. Retreive all existing courses info \n 2. Select a course and get its details" \
        "\n 3. Add a course with its info \n 4. Modify course info \n 5. Delete course info" \
        "Type the number to proceed, or Type 0 to exit.")

command = input()

# Proceed to task
import dotask

while command != 0:
    if len(command) == 1:
        match int(command):
            case 1: dotask.GetAllCourse(cursor)
            #case 2: dotask.SearchBy(cursor)
            case 3: dotask.AddCourse(cursor, _db)
            case 4: dotask.ModifyCourse(cursor, _db)
            case 5: dotask.DeleteCourse(cursor, _db)
            case 0: break
            case _: print("Typed Wrong")

        # Task Ended, Ask for another task
        print("Task completed! Is anything to do more? \n 1. Retreive all existing courses \n 2. Select a course and get its details" \
            "\n 3. Add a course with its info \n 4. Modify course info \n 5. Delete course info" \
            "Type the number to proceed, or Type 0 to exit.")
        command = input()
    else:
        print("Type Valid number")
        command = input()

# Disconnect from MySQL
cursor.close()
db.close()
print("Thank you")
