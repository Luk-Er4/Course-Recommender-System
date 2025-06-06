import os
from pathlib import Path

##### Get the """FACT""" from a transcript
def transcript_choose():
    # Show Transcript List
    transcript_dir = Path("data/transcript")
    transcript_lst = os.listdir(transcript_dir)

    # Choose what transcript
    print("Here is the list of transcripts.")
    print(transcript_lst)
    print("Which transcript do you use?")

    good_to_go = True

    while good_to_go:
        transcript = input("")
        if transcript not in transcript_lst:
            print("You typed wrong!")
        else:
            print("Thanks for responding!")
            good_to_go = False

    transcript_path = transcript_dir / transcript

    # Open the Transcript
    with open(transcript_path, "r") as file:
        if file:
            content = file.read()
            print(content)                                        # Debug purpose

    # Get the Course Code and Grade
    course_grade = content.split("\n")

    # Remove empty strings from course_grade
    course_grade = [line for line in course_grade if line]  # Keep only non-empty lines

    return course_grade, transcript