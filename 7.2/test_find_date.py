"""Verify if the function find_date correctly parses and returns the
month, day, and year of a date found in a given string.
"""
import make_european

def test_find_date():
    """Assert correct return order and values of the find_date
    function.
    """
    # Expected input.
    assert make_european.find_date('01/25/1984:coit125@aol.com') == ('1', '25', '1984')
    # Check months with 31 days.
    assert make_european.find_date('01/31/1984:coit125@aol.com') == ('1', '31', '1984')
    # Check months with 30 days.
    assert make_european.find_date('11/30/1983:orangelover1107@hanmail.net') == ('11', '30', '1983')
    # Check February.
    assert make_european.find_date('02/28/1980:valentinelover@hearts.net') == ('2', '28', '1980')
    # Check return order.
    assert make_european.find_date('01/25/1984:coit125@aol.com') != ('25', '1', '1984')
