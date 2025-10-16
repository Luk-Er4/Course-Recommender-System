# Start
print("This is Admin software for accessing course data.")

# Initialize the software for admin
import sqlconnector_admin

while True:
    connection, db = sqlconnector_admin.connectSQL()
    if connection == True:
        cursor = db.cursor()
        break

# Entered Admin / Choose Tasks 
print("You have an authority to \n 1. Retreive all existing courses \n 2. Select a course and get its details" \
        "\n 3. Add a course with its info \n 4. Modify course info \n 5. Delete course info" \
        "Type the number to proceed, or Type 0 to exit.")

command = int(input())

# Proceed to task
import dotask

while command != 0:
    match command:
        case 1:
            print("Do 1")
            dotask.GetAllCourse(cursor)
        case 2:
            print("Do 2")
            dotask.SearchBy(cursor)
        case 3:
            print("Do 3")
            dotask.AddCourse(cursor)
        case 4:
            print("Do 4")
            dotask.ModifyCourse(cursor)
        case 5:
            print("Do 5")
            dotask.DeleteCourse(cursor)
        case _:
            print("Typed Wrong")

    # Task Ended, Ask for another task
    print("Task completed! Is anything to do more? \n 1. Retreive all existing courses \n 2. Select a course and get its details" \
        "\n 3. Add a course with its info \n 4. Modify course info \n 5. Delete course info" \
        "Type the number to proceed, or Type 0 to exit.")

    command = int(input())

# Disconnect from MySQL
cursor.close()
db.close()
print("Thank you")
