"""Verify if the function convert_input returns the username of the
specified host addresses with their corresponding dates converted to
European format.
"""
import make_european

def test_convert_input():
    """Assert correct output for the function convert_input when the
    host address matches and does not match the host address found in
    first string parameter.
    """
    # Expected input.
    assert make_european.convert_input('01/25/1984:coit125@aol.com',
                                       'aol.com') == '25/1/1984 coit125'
    # Check different email address input.
    assert make_european.convert_input('04/20/1983:jobethegreat@hotmail.com',
                                       'hotmail.com') == '20/4/1983 jobethegreat'
    # Check different email address extension.
    assert make_european.convert_input('04/20/1983:jobethegreat@att.net',
                                       'att.net') == '20/4/1983 jobethegreat'
    # Check when desired host name and host input are similar.
    assert not make_european.convert_input('01/25/1984:coit125@fake.aol.com',
                                           'aol.com')
    # Check capitalized email address.
    assert make_european.convert_input('01/25/1984:COIT125@AOL.com',
                                       'aol.com') == '25/1/1984 coit125'
    # Check Euro conversion.
    assert make_european.convert_input('11/07/1983:orangelover1107@hanmail.net',
                                       'hanmail.net') != '11/7/1983 orangelover1107'
