"""Verify the correct output of the function easy_way."""
import reverse_string

def test_easy_way():
    """Assert the correct return value for various inputs given to the
    easy_way function.
    """
    # Anticipated input.
    assert reverse_string.easy_way('The quick brown fox jumped over the lazy dog.'
                                  ) == '.god yzal eht revo depmuj xof nworb kciuq ehT'
    # 1 input.
    assert reverse_string.easy_way('A') == 'A'
    # No input.
    assert reverse_string.easy_way('') == ''
    # Odd number of input.
    assert reverse_string.easy_way('12345') == '54321'
    # Even number of input.
    assert reverse_string.easy_way('1234') == '4321'
