"""Verify the correct reversal of the items in a list given to the
function reverse.
"""
from reverse_string import reverse

def test_reverse():
    """Assert the correct order of items in a returned list of various
    list inputs for the reverse function.
    """
    # Anticipated input.
    assert reverse(['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
                  ) == ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'H']
    # 1 input.
    assert reverse(['A']) == ['A']
    # No input.
    assert reverse([]) == []
    # Odd number of input.
    assert reverse(['1', '2', '3']) == ['3', '2', '1']
    # Even number of input.
    assert reverse(['1', '2', '3', '4']) == ['4', '3', '2', '1']
