import json
from pathlib import Path

##### Get the """DATA""" from json
def course_data_collection():
    # Get the json file that contains course information
    file_path = Path("data/coursejson/course_descriptions_6.json")

    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    #1. Course Codes
    course_codes = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
    ]

    #2. Course Names
    course_names = [
        course["name"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
    ]

    #3. Available Courses
    course_available = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("unavailable") != True
    ]

    #4. Total Topics from Courses
    topics = list(set(
        course["topic"]
        for subject in data["ASUcourses"]
        if subject["subject"] == "Computer Science"
        for course in subject["courses"]
        if course.get("unavailable") != True # e.g. Image Processing is not available so take it out
    ))

    #5. Topic for Each Courses
    course_topics = [
        [course["code"], course["topic"]]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
    ]

    #6. Prerequisites for Each Course
    course_AND_prerequisites = [
        [course["code"], course["prereq"]]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if "prereq" in course
    ]

    #7. Core Courses for CS Majors
    course_req_cs_major = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("coreCSmajor") == True
    ]

    #8. Elective Courses for CS Majors
    course_elt_cs_major = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("coreCSmajor") != True
    ]

    ##### S2
    #9. Core Courses for Cyber Majors
    course_req_cy_major = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("coreCYmajor") == True
    ]

    #10. Elective Courses for Cyber Majors
    course_elt_cy_major = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("coreCYmajor") != True
    ]

    ##### S4
    #11. OR Prerequisites for Each Course
    course_OR_prerequisites = [
        [course["code"], course["prereq(OR)"]]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if "prereq(OR)" in course
    ]

    #12. Core-requisites for Each Course
    course_core_quisites = [
        [course["code"], course["corequisite"]]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if "corequisite" in course
    ]

    ##### S5
    #13. Core Courses for CS Minors
    course_req_cs_minor = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("reqCSminor") == True
    ]

    #14. Elective Courses for CS Minors
    course_elt_cs_minor = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("eltCSminor") == True
    ]

    #15. Core Courses for Cyber Minors
    course_req_cy_minor = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("reqCYminor") == True
    ]

    #16. Elective Courses for Cyber Minors
    course_elt_cy_minor = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("eltCYminor") == True
    ]

    ##### S6
    #17. Courses that requires Approval
    course_approval_prerequisite = [
        course["code"]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if course.get("preapproval") == True
    ]

    #18. Courses that requires Approval
    course_standing_prerequisite = [
        [course["code"], course["prestandings"]]
        for subject in data["ASUcourses"]
        for course in subject["courses"]
        if "prestandings" in course
    ]

    print("course_codes                 ", course_codes)
    print("course_names                 ", course_names)
    print("course_available             ", course_available)
    print("topics                       ", topics)
    print("course_topics                ", course_topics)
    #print("course_AND_prerequisites     ", course_AND_prerequisites)
    print("course_req_cs_major          ", course_req_cs_major)
    #print("course_elt_cs_major ", course_elt_cs_major)
    ##### S2
    print("course_req_cy_major          ", course_req_cy_major)
    #print("course_elt_cy_major ", course_elt_cy_major)
    ##### S4
    print("course_OR_prerequisites      ", course_OR_prerequisites)
    print("course_core_quisites         ", course_core_quisites)
    ##### S5
    print("course_req_cs_minor          ", course_req_cs_minor)
    print("course_elt_cs_minor          ", course_elt_cs_minor)
    print("course_req_cy_minor          ", course_req_cy_minor)
    print("course_elt_cy_minor          ", course_elt_cy_minor)
    ##### S6
    print("course_approval_prerequisite ", course_approval_prerequisite)
    print("course_standing_prerequisite ", course_standing_prerequisite)

    return course_codes, course_names, course_available, topics, course_topics, course_AND_prerequisites, course_req_cs_major, course_elt_cs_major, course_req_cy_major, course_elt_cy_major, course_OR_prerequisites, course_core_quisites, course_req_cs_minor, course_elt_cs_minor, course_req_cy_minor, course_elt_cy_minor, course_approval_prerequisite, course_standing_prerequisite, data
