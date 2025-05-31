# student infos
def student_infos(student_interests, interested_certificates, student_major, student_minor, advised_semester):
    print("Student interests: ", student_interests)
    print("Interested Certificates: ", interested_certificates)
    print("Student Major/Minor:", student_major, "/", student_minor)
    print("Advised Semester:", advised_semester)
    print("")

# recommendation lists
def recommendation_list(MajorInterestRecommendations, CertificateRecommendations, MajorCoreRecommendations, MinorCoreRecommendations, RecommendedCourses, advised_semester, AvailableCourses, wavied_course, ismajor, isminor):
    print("These are courses that you can take that match your interests based on current status:", sorted(MajorInterestRecommendations))
    print("These are courses that you can take that match your interested certificates:", sorted(CertificateRecommendations))
    if ismajor:
        print("These are courses not taken that fit your major core requirements:", sorted(MajorCoreRecommendations))
    if isminor:
        print("These are courses not taken that fit your minor core requirements:", sorted(MinorCoreRecommendations))
    print("These are the courses you can take:", sorted(RecommendedCourses))
    print("")
    print("These are the recommended courses for **", advised_semester, "** semester: ", sorted(AvailableCourses))
    if len(wavied_course) != 0:
        print("Waived for such courses:", wavied_course)