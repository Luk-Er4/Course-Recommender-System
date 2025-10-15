import sqlconnector_admin
# Initialize the software for admin
print("This is Admin software for accessing course data.")

while not sqlconnector_admin.connectSQL():
    print("Error occurred! Try again...")

cursor = sqlconnector_admin.connectSQL().cursor()

# Entered Admin mode
print("You have an authority to \n 1. Retreive all existing courses \n 2. Select a course and get its details" \
        "\n 3. Add a course with its info \n 4. Modify course info \n 5. Delete course info")

