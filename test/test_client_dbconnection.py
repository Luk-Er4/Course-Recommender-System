import src_client.sqlconnector_client as ssc

def test_sqlconnector_client():
    assert ssc.connectSQL()[0] == True

