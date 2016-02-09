"""Verify if the function is_valid correctly determines the validity of
of a given input.
"""
from make_european import is_valid

def test_is_valid():
    """Assert correct boolean for various inputs given to is_valid."""
    # Expected input.
    assert is_valid('12/31/2015:john.a.graham@gmail.com')
    # Check 'at' typo.
    assert not is_valid('12/31/2015:john.a.grahamgmail.com')
    # Check colon typo.
    assert not is_valid('12/31/2015::john.a.graham@gmail.com')
    # Check forward slash replacement.
    assert not is_valid('12.31.2015:john.a.graham@gmail.com')
    # Check order.
    assert not is_valid('john.a.graham@gmail.com:12/31/2015')
