import os
from pathlib import Path

def check_waiver(transcript, testing = False):
    # Check Wavier by tracking student name
    wavier_dir = Path("data/Wavier for Students")
    wavier_lst = os.listdir(wavier_dir)

    wavied_course = []
    target_wavier = transcript[:-4] + "_Wavier.txt"
    there_is_wavier = False

    if target_wavier in wavier_lst:
        there_is_wavier = True
        if testing:
            with open(str(wavier_dir) + "/" + target_wavier, "r") as file:    
                content = file.read()
        else:
            with open(str(wavier_dir) + "\\" + target_wavier, "r") as file:
                content = file.read()
            print(content)

    if there_is_wavier:
        # Get the Course Code and Grade
        w_course = content.split("\n")

        # Remove empty strings from course_grade
        w_course = [line for line in w_course if line]  # Keep only non-empty lines

        for i in range(len(w_course)):
            wavied_course.append(w_course[i])
    
    return wavied_course