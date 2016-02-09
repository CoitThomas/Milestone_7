"""Verify if the function make_int converts a number in string form
into a number in integer form and returns it. If the string does not
contain a number, verify that the functions returns None.
"""
import make_european

def test_make_int():
    """Assert the correct return of an integer or None for the function
    make_int given a number in string form.
    """
    # Expected input.
    assert make_european.make_int('1') == 1
    # Check non-number string
    assert make_european.make_int('one') is None
    # Check float number string
    assert make_european.make_int('1.1') is None
