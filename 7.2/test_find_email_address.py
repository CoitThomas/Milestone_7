"""Verify if the function find_email_address correctly parses and
returns the username and host of an email address found in a given
string.
"""
import make_european

def test_find_email_address():
    """Assert correct return order and values of the find_email_address
    function.
    """
    # Expected input.
    assert make_european.find_email_address('11/07/1984:orangelover1107@hanmail.net'
                                           ) == ('orangelover1107', 'hanmail.net')
    # Check username output.
    assert make_european.find_email_address('11/07/1984:gant_007@hotmail.com'
                                           ) != ('gant_007@', 'hotmail.com')
    # Check host output.
    assert make_european.find_email_address('11/07/1984:sterlingsmile@msn.com'
                                           ) != ('sterlingsmile', '@msn.com')
    # Check return order.
    assert make_european.find_email_address('11/07/1984:kate2345@msn.com'
                                           ) != ('msn.com', 'kate2345')
    # Check input with misc. characters.
    assert make_european.find_email_address('!@#11/07/1984:coit125@aol.com^&*',
                                           ) == ('coit125', 'aol.com')
