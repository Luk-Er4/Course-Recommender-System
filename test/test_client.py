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
    assert check_pass_or_fail(case3) == pass3

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

