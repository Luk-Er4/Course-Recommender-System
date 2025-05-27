# check the student passed or failed in each course
def check_pass_or_fail(course_grade):
    # F is "failed", the others are "passed"
    passed_courses = []

    for i in range(len(course_grade)):
        letter_grade = course_grade[i][-1]
        if letter_grade != "F":
            passed_courses.append(course_grade[i][0:-2])
        else:
            pass

    return passed_courses