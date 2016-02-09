"""Verify if the function is_valid_date correctly determins the
validity of given integer representations of a date.
"""
import make_european

def test_is_valid_date():
    """Assert correct validation for various integer inputs for the
    function is_valid_date.
    """
    # Expected input.
    assert make_european.is_valid_date(1, 25, 1984)
    # Check month
    assert not make_european.is_valid_date(-1, 25, 1984)
    assert not make_european.is_valid_date(13, 25, 1984)
    # Check day
    assert not make_european.is_valid_date(1, 32, 1984)
    assert not make_european.is_valid_date(1, 0, 1984)
    assert not make_european.is_valid_date(4, 31, 1984)
    assert not make_european.is_valid_date(2, 30, 1984)
    # Check year
    assert not make_european.is_valid_date(1, 25, 198444)
    assert not make_european.is_valid_date(1, 25, -1)
