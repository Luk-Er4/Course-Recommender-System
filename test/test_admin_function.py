import src_admin.dotask as sd

def test_isColName():
    cases = ["name", "subject", "title", "test", "learn", "preapproval", "AvailF"]
    passs = [True, True, False, False, False, True, False]

    for i in range(len(cases)):
        assert sd.IsColName(cases[i]) == passs[i]

def test_CheckDuplicates():
    cases_code = ["CS1314", "CS999999999", "MATH7654321", "MATH2312"]
    passs_code = [True, False, False, True]
    cases_name = ["Research", "Ultimate Mathematics", "Computer Science I", "Great Computers"]
    passs_name = [True, False, True, False]

    for i in range(len(cases_code)):
        assert sd.CheckDuplicates(cases_code[i], "code") == passs_code[i]
    for i in range(len(cases_name)):
        assert sd.CheckDuplicates(cases_name[i], "name") == passs_name[i]

def test_CheckValidChars():
    cases_target = ["Calculus", "Ultimate Computer Science", "a b c d e f g h", "select * from asu_courses", "delete *", ""]
    passs_target = [True, True, False, False, False, True] 
    cases_others = ["Division", "Ddos Attack", "order by courses", "mathe_matics", "Learning", ""]
    passs_others = [True, False, False, False, True, True]

    for i in range(len(cases_target)):
        assert sd.CheckValidChars(cases_target[i], "subject") == passs_target[i]
    for i in range(len(cases_others)):
        assert sd.CheckValidChars(cases_others[i], "code") == passs_others[i]

# def test_IsValidInput(info, checkDup = "Y")

