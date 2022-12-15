import pytest
from UI_Funcs import *
from db_utils import *
from io import StringIO
from testfixtures import TempDirectory

''' Automated Unit Testing Python File for four functions of our choice'''


#FIRST FUNCTION TESTS
def test_yes_or_No(monkeypatch,capfd):

    test_string = 'yes'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert yes_or_No() == 'yes'

    # out, err = capfd.readouterr()
    # assert out == 'Would you like to execute another query? (yes/no): '





    #assert test_yes_or_No(yes) ==
    # assert test_yes_or_No("no")
    # assert test_yes_or_No(" ")
    # assert test_yes_or_No(None)
    # assert test_yes_or_No(64)


#SECOND FUNCTION TESTS
#def test__make_tables():



#THIRD FUNCTION TESTS




#FOURTH FUNCTION TESTS
