### survey section

# get major info
def major_info():
    # Get the major info
    print("What is your major? Computer Science, Cybersecurity")
    good_to_go = True

    # Major list
    major_list = ['Computer Science', "Cybersecurity"]

    # Student Major
    student_major = []

    print("What is your major?")
    print("1. BS in Computer Science")
    print("2. BS in Cybersecurity")
    print("3. BS in Computer Science and Cybersecurity")
    print("0. I am working on Minor Program")

    while good_to_go:
        major = input(" type the number, 1, 2 or 3: ")
        if major == "1":
            student_major = ['Computer Science']
            good_to_go = False
        elif major == "2":
            student_major = ['Cybersecurity']
            good_to_go = False
        elif major == "3":
            student_major = ['Computer Science', 'Cybersecurity']
            good_to_go = False
        elif major == "0":
            student_major = []
            good_to_go = False
        else:
            print("You typed wrong!")
        print("Thanks for responding!")

    return student_major

# get minor info
def minor_info():
    # Get the minor info
    print("What is your minor? Computer Science, Cybersecurity")
    good_to_go = True

    # Minor list
    minor_list = ['Computer Science', "Cybersecurity"]

    # Student Major
    student_minor = []

    print("What is your minor?")
    print("1. Minor in Computer Science")
    print("2. Minor in Cybersecurity")
    print("3. Minor in Computer Science and Cybersecurity")
    print("0. I do not work on Minor Programs")

    while good_to_go:
        major = input(" type the number, 1, 2 or 3: ")
        if major == "1":
            student_minor = ['Computer Science']
            good_to_go = False
        elif major == "2":
            student_minor = ['Cybersecurity']
            good_to_go = False
        elif major == "3":
            student_minor = ['Computer Science', 'Cybersecurity']
            good_to_go = False
        elif major == "0":
            student_minor = []
            good_to_go = False
        else:
            print("You typed wrong!")
        print("Thanks for responding!")

    return student_minor

# get semester info
def semester_info():
    # What semester the student is taking courses in
    print("You are getting recommendation for...")
    print("1. Fall 2. Spring 3. Summer Semester.")

    good_to_go = True

    while good_to_go:
        major = input(" type the number, 1, 2 or 3: ")
        if major == "1":
            advised_semester = "Fall"
            good_to_go = False
        elif major == "2":
            advised_semester = "Spring"
            good_to_go = False
        elif major == "3":
            advised_semester = "Summer"
            good_to_go = False
        else:
            print("You typed wrong!")
    print("Thanks for responding!")

    return advised_semester

# get topic info
def topic_info(topics):
    # Ask Interested Topics
    student_interests = []
    good_to_go = True

    print(topics)
    while good_to_go:
        interest = input("\nHere are the topics we have. Choose the topic one by one. If you want to stop, type STOP.")
        if interest == "STOP" and len(student_interests) == 0:
            print("You need to put at least one topic!")
        elif interest == "STOP" and len(student_interests) != 0:
            print("Thanks for responding!")
            good_to_go = False
        elif interest not in topics:
            print("You typed wrong!")
        else:
            student_interests.append(interest)
    
    return student_interests

# get standing info
def standing_info():
    # Ask what year the student in
    good_to_go = True

    while good_to_go:
        year = input("What is your classification? 1. Freshmen 2. Sophomore 3. Junior 4. Senior")
        if year == "1":
            student_classification = ["Freshmen"]
            good_to_go = False
        elif year == "2":
            student_classification = ["Freshmen", "Sophomore"]
            good_to_go = False
        elif year == "3":
            student_classification = ["Freshmen", "Sophomore", "Junior"]
            good_to_go = False
        elif year == "4":
            student_classification = ["Freshmen", "Sophomore", "Junior", "Senior"]
            good_to_go = False
        else:
            print("You typed wrong!")
    print("Thanks for responding!")

    return student_classification

# get certification info
def certification_info():
    interested_certificates = []
    data2 = {"certificates": [
            {
                "subject": "Computer Science",
                "certificate": [
                    {
                        "name": "Computer Game Development",
                        "courses": ["CS3371", "CS3372", "CS4318", "CS4371"]
                    },
                    {
                        "name": "Cybersecurity Technologies",
                        "courses": ["CS3310", "CS4314", "CS4320",{
                        "options": ["BOR3307", "BOR3309", "BOR4305", "CS4340"]
                        }
                        ]
                    },
                    {
                        "name": "Data Science",
                        "courses": ["CS1314", "CS4318", "CS4319", "CS4330"]
                    },
                    {
                        "name": "Web and Mobile Development",
                        "courses": ["CS3312", "CS3372", "CS4312",{
                        "options": ["CS1314", "CS1351"]
                        }
                        ]
                    }
                ]
            }
    ]
    }
    certificate_list = [cert["name"] for cert in data2["certificates"][0]["certificate"]]
    good_to_go = True

    print(certificate_list)
    while good_to_go:
        certificate = input("\nHere are the certificates we have. Choose the certificates one by one. If you want to stop, type STOP.")
        if certificate == "STOP":
            print("Thanks for responding!")
            good_to_go = False
        elif certificate not in certificate_list:
            print("You typed wrong!")
        else:
            interested_certificates.append(certificate)
    
    return interested_certificates, data2