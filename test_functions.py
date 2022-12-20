"""
Automated Unit Testing Python File for four functions
"""

import pytest
from UI_Funcs import *
from io import StringIO


def test_is_nums():
    """Unit Test Function for is_nums"""
    assert is_nums('13') == True
    assert is_nums('22000') == True
    assert is_nums('Jaylen Brown') == False
    assert is_nums('22 \n') == False
    assert is_nums(' ') == False
    assert is_nums('\n') == False
    with pytest.raises(AttributeError) as error:
        is_nums(None)
    assert error.type is AttributeError
    with pytest.raises(AttributeError) as error:
        is_nums(13)
    assert error.type is AttributeError


def test_stars_Equality(monkeypatch, capfd):
    """TESTS FUNCTION for the UI_Funcs.py function: stars_equality"""
    # TEST 1: TESTS INPUT OF '>'
    test_string = '>'
    simulated_input = StringIO(test_string)
    monkeypatch.setattr('sys.stdin', simulated_input)
    assert stars_Equality() == '>'

    # TEST 2: TESTS CORRECT PROMPT IS PRINTED TO TERMINAL
    out, err = capfd.readouterr()
    assert out == 'Choose an equality operator (>, <, >=, <=, =): '

    # TEST 3: TESTS INPUT OF '<'
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

    # TEST 6: TESTS INPUT OF '='
    test_string5 = '='
    simulated_input5 = StringIO(test_string5)
    monkeypatch.setattr('sys.stdin', simulated_input5)
    assert stars_Equality() == '='

    # TEST 7: TESTS INVALID INPUT VALUE OF STRING 'Jaylen Brown'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('Jaylen Brown\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError

    # TEST 8: TESTS INVALID INPUT VALUE OF AN INTEGER
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('10\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError

    # TEST 9: TESTS INVALID INPUT OF EMPTY LINE
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(' ')
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError

    # TEST 10: TESTS INVALID INPUT OF NONE
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(None)
        monkeypatch.setattr('sys.stdin', number_inputs)
        stars_Equality()
    assert error.type is EOFError


def test_has_dot():
    """Unit Test for function has_dot"""
    assert has_dot('13') == False
    assert has_dot('19.99') == True
    assert has_dot('KG') == False
    assert has_dot('\n') == False
    assert has_dot(' ') == False
    with pytest.raises(AttributeError) as error:
        has_dot(13)
    assert error.type is AttributeError


def test_review_Target(monkeypatch, capfd):
    """TESTS FUNCTION for the UI_Funcs.py function: review_Target"""
    # TEST 1: TESTS INPUT OF NORMAL VALID INPUT NUMBER '1000'
    number_inputs = StringIO('1000\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    assert reviews_Target() == 1000

    # TEST 2: TESTS CORRECT PROMPT IS PRINTED TO TERMINAL
    out, err = capfd.readouterr()
    assert out == "Enter a target number of reviews (ex. 1000): \n\n"

    # TEST 3: TESTS INVALID INPUT VALUE OF STRING 'Jaylen Brown'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('Jaylen Brown\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    # TEST 4: TESTS INVALID INPUT OF TOO HIGH VALUE '1000000000000000'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('1000000000000000\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    # TEST 5: TESTS INVALID INPUT OF TOO LOW VALUE '-10'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('-10\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    # TEST 6: TESTS INVALID INPUT OF NOTHING ' '
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(' ')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    # TEST 7: TESTS INVALID INPUT OF JUST NEW LINE '\n'
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO('\n')
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError

    # TEST 8: TESTS INVALID INPUT OF NONE
    with pytest.raises(EOFError) as error:
        number_inputs = StringIO(None)
        monkeypatch.setattr('sys.stdin', number_inputs)
        reviews_Target()
    assert error.type is EOFError
