from src_client.checkpassorfail import check_pass_or_fail

def test_check_pass_or_fail():
    case1 = ['CS1351 B', 'CS1336 C', 'CS2324 F', 'CS1391 B', 'MATH2305 D']
    pass1 = ['CS1351', 'CS1336', 'CS1391', 'MATH2305']
    case2 = ['CS1371 F', 'CS1332 F', 'CS2300 F', 'CS1391 D', 'MATH2305 D']
    pass2 = ['CS1391', 'MATH2305']
    case3 = []
    pass3 = []

    assert check_pass_or_fail(case1) == pass1
    assert check_pass_or_fail(case2) == pass2
    assert check_pass_or_fail(case3) == case3

from src_client.checkwaiver import check_waiver

def test_check_waiver():
    case1 = "Ashley_Smith.txt"
    pass1 = ["CS1191"]
    case2 = "Michael_Lawrence.txt"
    pass2 = ["CS4091"]
    case3 = "Max_Powell.txt"
    pass3 = []

    assert check_waiver(case1) == pass1
    assert check_waiver(case2) == pass2
    assert check_waiver(case3) == pass3

import src_client.main_client as cm 

def test_isCSMajor(monkeypatch):
    case1 = ["Computer Science"]
    pass1 = True
    case2 = ["Cybersecurity"]
    pass2 = False
    case3 = ["Computer Science", "Cybersecurity"]
    pass3 = True
    case4 = []
    pass4 = False

    monkeypatch.setattr(cm, "student_major", case1)
    assert cm.isCSMajor() == pass1
    monkeypatch.setattr(cm, "student_major", case2)
    assert cm.isCSMajor() == pass2    
    monkeypatch.setattr(cm, "student_major", case3)
    assert cm.isCSMajor() == pass3    
    monkeypatch.setattr(cm, "student_major", case4)
    assert cm.isCSMajor() == pass4