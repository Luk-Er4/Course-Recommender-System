import src_admin.sqlconnector_admin as ssa

def test_sqlconnector_admin():
    assert ssa.connectSQL()[0] == True

