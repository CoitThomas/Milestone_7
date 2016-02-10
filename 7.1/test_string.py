"""Verify the correct returned string value of a list of chars given
to the funtion string().
"""
from reverse_string import string

def test_string():
    """Assert the correct returned string values for various lists of
    chars given to the string() function.
    """
    # Anticipated input.
    assert string(['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']) == 'Hello world'
    # 1 input.
    assert string(['A']) == 'A'
    # No input.
    assert string([]) == ''
