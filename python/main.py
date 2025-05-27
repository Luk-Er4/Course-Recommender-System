# Get all required library
import json
import os

# get course infos
import coursedata

temp = coursedata.course_data_collection()
course_codes = temp[0]
course_names = temp[1]
course_available = temp[2]
topics = temp[3] 
course_topics = temp[4]
course_AND_prerequisites = temp[5]
course_req_cs_major = temp[6]
course_elt_cs_major = temp[7]
course_req_cy_major = temp[8]
course_elt_cy_major = temp[9]
course_OR_prerequisites = temp[10]
course_core_quisites = temp[11]
course_req_cs_minor = temp[12]
course_elt_cs_minor = temp[13]
course_req_cy_minor = temp[14]
course_elt_cy_minor = temp[15]
course_approval_prerequisite = temp[16]
course_standing_prerequisite = temp[17]
data = temp[18]

# get transcript infos
import transcriptchoose
temp = transcriptchoose.transcript_choose()
course_grade = temp[0]
transcript = temp[1]

# get pass or fail infos
import checkpassorfail
passed_courses = checkpassorfail.check_pass_or_fail(course_grade)
  
# get waiver infos
import checkwaiver
wavied_course = checkwaiver.check_waiver(transcript)

### survey section
import studentsurvey

# get the major info
student_major = studentsurvey.major_info()

# get the minor info
student_minor = studentsurvey.minor_info()

# get semester info
advised_semester = studentsurvey.semester_info()

# get certification preference info
temp = studentsurvey.certification_info()
interested_certificates = temp[0]
cert_data = temp[1]

# get interested topics info
student_interests = studentsurvey.topic_info(topics)

# get standing info
student_classification = studentsurvey.standing_info()

###########################################################################
############################### predicates ################################
###########################################################################

def courseinfo(code):
    for subject in data["ASUcourses"]:
        for c in subject["courses"]:
            if c["code"] == code:
                return c
    return None

def isAvailable(code):
    return code in course_available

def HasPassed(code):
    return code in passed_courses

def PassedANDPrereqs(code):
    course = courseinfo(code)
    prereqs = course.get("prereq", [])
    return all(prereq in passed_courses for prereq in prereqs)

def MatcheInterest(code):
    course = courseinfo(code)
    return course["topic"] in student_interests

def IsCoreMajor(code):
    return ((isCSMajor() and isCoreCSMajor(code)) or
            (isCYMajor() and isCoreCYMajor(code)))

##### S2
def isCSMajor():
    return "Computer Science" in student_major

def isCYMajor():
    return "Cybersecurity" in student_major

def isCoreCSMajor(code):
  return code in course_req_cs_major

def isCoreCYMajor(code):
  return code in course_req_cy_major

##### S3
def isAvailableSemester(code):
    return advised_semester in courseinfo(code).get("availsemester", [])

##### S4
def PassedORPrereqs(code):
    course = courseinfo(code)
    or_prereqs = course.get("prereq(OR)", [])
    return len(or_prereqs) == 0 or any(prereq in passed_courses for prereq in or_prereqs)

##### S5
def isCSMinor():
    return "Computer Science" in student_minor

def isCYMinor():
    return "Cybersecurity" in student_minor

def isCoreCSMinor(code):
  return code in course_req_cs_minor

def isCoreCYMinor(code):
  return code in course_req_cy_minor

def IsCoreMinor(code):
    return ((isCSMinor() and isCoreCSMinor(code)) or
            (isCYMinor() and isCoreCYMinor(code)))

def IsMinorElective(code):
    return ((isCSMinor() and isCoreCSMinor(code)) or
            (isCYMinor() and isCoreCYMinor(code)))

##### S6
def PassedApprovalPrereqs(code):
    return (not CheckApprovalPrereqs(code)) or (code in wavied_course)

def CheckApprovalPrereqs(code):
    return code in course_approval_prerequisite

def PassedStandingPrereqs(code):
    standing_prereqs = courseinfo(code).get("prestandings")
    return (not CheckStandingPrereqs(code)) or (standing_prereqs in student_classification)

def CheckStandingPrereqs(code):
    return code in course_standing_prerequisite

##### S7
def IsCertificatesCourse(code, data2):
  for subject_area in data2["certificates"]:
    for cert in subject_area["certificate"]:
      for course in cert["courses"]:
        if course == code:
          return True
        if isinstance(course, dict) and "options" in course:
          if code in course["options"]:
            return True
  return False

########################################################################

MajorInterestRecommendations = [
    code for code in course_codes
    if (isCSMajor() or isCYMajor())
    and isAvailable(code)
    and not HasPassed(code)
    and PassedANDPrereqs(code)
    and PassedORPrereqs(code)
    and MatcheInterest(code)
]

MajorCoreRecommendations = [
    code for code in course_codes
    if IsCoreMajor(code) and not HasPassed(code)
]

MinorInterestRecommendations = [
    code for code in course_codes
    if (isCSMinor() or isCYMinor())
    and isAvailable(code)
    and not HasPassed(code)
    and PassedANDPrereqs(code)
    and PassedORPrereqs(code)
    and MatcheInterest(code)
    and IsMinorElective(code)
]

MinorCoreRecommendations = [
    code for code in course_codes
    if IsCoreMinor(code) and not HasPassed(code)
]
CertificateRecommendations = [
    code for code in course_codes
    if IsCertificatesCourse(code, cert_data)
    and isAvailable(code)
    and not HasPassed(code)
    and PassedANDPrereqs(code)
    and PassedORPrereqs(code)
]

RecommendedCourses = [
    code for code in set(MajorInterestRecommendations + MajorCoreRecommendations + MinorInterestRecommendations + MinorCoreRecommendations + CertificateRecommendations)
    if PassedANDPrereqs(code) and PassedORPrereqs(code) and PassedApprovalPrereqs(code) and PassedStandingPrereqs(code)
]

AvailableCourses = [
    code for code in RecommendedCourses
    if isAvailableSemester(code)
]

#######################################################################################

### show the result
import recommendation

# student info
recommendation.student_infos(student_interests, interested_certificates, student_major, student_minor, advised_semester)

# recommended lists
recommendation.recommendation_list(MajorInterestRecommendations, CertificateRecommendations, MajorCoreRecommendations,
                                   MinorCoreRecommendations, RecommendedCourses, advised_semester, AvailableCourses, wavied_course, 
                                   ismajor = isCSMajor() or isCYMajor(), isminor = isCSMinor() or isCYMinor())

