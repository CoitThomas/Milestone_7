"""Take input in the format:
mm/dd/yyyy:username@host
Print out all of the usernames that have the host 'aol' and convert
the date to European format so that the following format is produced:
dd/mm/yyyy username
"""
import re
from get_input import get_input

def convert_input(string, desired_host):
    """Take in a string and a desired host. If the host found in the
    string matches the desired host, then convert the found date to the
    European format and convert the username to all lowercase. Return
    the new date and username.
    """
    username, host = find_email_address(string)
    assert username and host, "A valid email address was not present in the given string."
    if host.lower() == desired_host.lower():
        month, day, year = find_date(string)
        euro_date = '%s/%s/%s' % (day, month, year) # Convert the date into European format.
        return '%s %s' % (euro_date, username.lower())

def find_email_address(string):
    """Take in a string and return the username and host of the email
    address found in the string.
    """
    assert isinstance(string, str), "The input for find_email_address needs to be a string."

    email_address = re.search( # search for username@host
        r"(?P<username>[\w.-]+)" # the username
        r"@(?P<host>[\w.-]+)", # the host
        string
    )
    assert email_address, "A proper email address must be provided."

    username = email_address.group('username')
    host = email_address.group('host')

    return (username, host)

def find_date(string):
    """Take in a string and return the month, day, and year of the date
    found in the string."""
    assert isinstance(string, str), "The function find_date takes a string."

    date = re.search( # search for mm/dd/yyyy
        "([0-9]{1,2})" # the month
        "/([0-9]{1,2})" # the day
        "/([0-9]{4})", # the year
        string
    )
    assert date, "A date in the format mm/dd/yyyy must be provided."

    month = int(date.group(1))
    day = int(date.group(2))
    year = int(date.group(3))

    assert 1 <= month <= 12, "Please enter a valid month."

    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    if month in month31:
        assert 1 <= day <= 31, "Please enter a valid day."
    if month in month30:
        assert 1 <= day <= 30, "Please enter a valid day."
    if month == 2:
        assert 1 <= day <= 28, "Please enter a valid day."

    assert 1900 <= year <= 2100, "Please enter a valid year."

    return (str(month), str(day), str(year))

if __name__ == "__main__":
    INPUT = get_input()
    HOST = 'aol.com' # Enter desired host here.
    while not INPUT.isspace() and INPUT:
        VALID_OUTPUT = convert_input(INPUT, HOST)
        if VALID_OUTPUT:
            print VALID_OUTPUT
        INPUT = get_input()
