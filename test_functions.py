import pytest
import requests

from UI_Funcs import *
from db_utils import *
from io import StringIO
from testfixtures import TempDirectory

''' Automated Unit Testing Python File for four functions'''


#FIRST FUNCTION TESTS
# def test_yes_or_No(monkeypatch,capfd):
#




#SECOND FUNCTION TESTS
# def test_get_request_check():
#



'''TESTS FUNCTION for the UI_Funcs.py function: stars_equality'''
def test_stars_Equality(monkeypatch, capfd):

    #TEST 1: TESTS INPUT OF '>'
    test_string = '>'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert stars_Equality() == '>'

    #TEST 2: TESTS CORRECT PROMPT IS PRINTED TO TERMINAL
    out, err = capfd.readouterr()
    assert out == 'Choose an equality operator (>, <, >=, <=, =): \n\n'

    #TEST 3: TESTS INPUT OF '<'
    test_string2 = '<'
    simulated_input2 = StringIO(test_string2)
    monkeypatch.setattr('sys.stdin', simulated_input2)
    assert stars_Equality() == '<'

    # TEST 4: TESTS INPUT OF '>='
    test_string3 = '>='
    simulated_input3 = StringIO(test_string3)
    monkeypatch.setattr('sys.stdin', simulated_input3)
    assert stars_Equality() == '>='

    # TEST 5: TESTS INPUT OF '<='
    test_string4 = '<='
    simulated_input4 = StringIO(test_string4)
    monkeypatch.setattr('sys.stdin', simulated_input4)
    assert stars_Equality() == '<='

    #TEST 6: TESTS INPUT OF '='
    test_string5 = '='
    simulated_input5 = StringIO(test_string5)
    monkeypatch.setattr('sys.stdin', simulated_input5)
    assert stars_Equality() == '='

    #TEST 7: TESTS INVALID INPUT VALUE OF STRING 'Jaylen Brown'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('Jaylen Brown\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError

    #TEST 8: TESTS INVALID INPUT VALUE OF AN INTEGER
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('10\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError

    #TEST 9: TESTS INVALID INPUT OF EMPTY LINE
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(' ')
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError

    #TEST 10: TESTS INVALID INPUT OF NONE
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(None)
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError





'''TESTS FUNCTION for the UI_Funcs.py function: review_Target'''
def test_review_Target(monkeypatch, capfd):

    #TEST 1: TESTS INPUT OF NORMAL VALID INPUT NUMBER '1000'
    number_inputs = StringIO('1000\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert reviews_Target() == 1000

    #TEST 2: TESTS CORRECT PROMPT IS PRINTED TO TERMINAL
    out, err = capfd.readouterr()
    assert out == "Enter a target number of reviews (ex. 1000): \n\n"

    #TEST 3: TESTS INVALID INPUT VALUE OF STRING 'Jaylen Brown'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('Jaylen Brown\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    #TEST 4: TESTS INVALID INPUT OF TOO HIGH VALUE '1000000000000000'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('1000000000000000\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    #TEST 5: TESTS INVALID INPUT OF TOO LOW VALUE '-10'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('-10\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    #TEST 6: TESTS INVALID INPUT OF NOTHING ' '
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(' ')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    #TEST 7: TESTS INVALID INPUT OF JUST NEW LINE '\n'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    #TEST 8: TESTS INVALID INPUT OF NONE
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(None)
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError










