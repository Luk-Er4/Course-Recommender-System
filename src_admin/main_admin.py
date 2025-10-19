# Start
print("This is Admin software for accessing course data.")

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
            case 1: dotask.GetAllCourse()
            case 2: dotask.SearchBy()
            case 3: dotask.AddCourse()
            case 4: dotask.ModifyCourse()
            case 5: dotask.DeleteCourse()
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
dotask.FinishTask()
print("Disconnected from server...")
print("Thank you")
