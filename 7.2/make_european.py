"""Take input in the format:
mm/dd/yyyy:username@host
Print out all of the usernames that have the host 'aol' and convert
the date to European format so that the following format is produced:
dd/mm/yyyy username
"""
import re
from get_input import get_input

REGEX_RULE = ("(?P<month>[0-9]{1,2})" # Month.
              "/(?P<day>[0-9]{1,2})" # Day.
              "/(?P<year>[0-9]{4})" # Year.
              r":(?P<username>[\w.-]+)" # Username.
              r"@(?P<host>[\w.-]+)" # Host.
             )

def make_int(string):
    """Convert a given string to an integer. If it cannot be converted,
    return None."""
    try:
        return int(string)
    except ValueError:
        return None

def is_valid(user_input):
    """Take input in the form of a string. Verify the string matches
    the format:
    mm/dd/yyyy:username@host
    Return True for valid, False for invalid.
    """
    assert isinstance(user_input, str), "Input must be a string."
    return re.search(REGEX_RULE, user_input)

def is_valid_date(month, day, year):
    """Take in three integers representing a month, day, and year.
    Verify they are valid representations and return True or False.
    """
    return valid_month(month) and valid_day(day, month) and valid_year(year)

def valid_month(month):
    """Take in an integer representing a month of the year. Return True
    if it is valid. Otherwise, return False.
    """
    return 1 <= month <= 12

def valid_day(day, month):
    """Take in an integer representing a day and month of the year.
    Return True if it is a valid day for the given month. Otherwise,
    return False.
    """
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    assert valid_month(month)
    if month in month31:
        return 1 <= day <= 31
    if month in month30:
        return 1 <= day <= 30
    if month == 2:
        return 1 <= day <= 28

def valid_year(year):
    """Take in an integer representing a pertinent year. Return True if
    it is valid. Otherwise, return False.
    """
    return 1900 <= year <= 2100

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
    data = re.search(REGEX_RULE, string)
    assert data, "An input in the format mm/dd/yyyy:username@host must be provided."

    username = data.group('username')
    host = data.group('host')

    return (username, host)

def find_date(string):
    """Take in a string and return the month, day, and year of the date
    found in the string."""
    assert isinstance(string, str), "The function find_date takes a string."
    data = re.search(REGEX_RULE, string)
    assert data, "An input in the format mm/dd/yyyy:username@host must be provided."

    month = make_int(data.group('month'))
    day = make_int(data.group('day'))
    year = make_int(data.group('year'))

    if is_valid_date(month, day, year):
        return (str(month), str(day), str(year))

if __name__ == "__main__":
    INPUT = get_input()
    HOST = 'aol.com' # Enter desired host here.
    while not INPUT.isspace() and INPUT:
        if is_valid(INPUT):
            OUTPUT = convert_input(INPUT, HOST)
            if OUTPUT:
                print OUTPUT
            INPUT = get_input()
        else: # Skip it and continue on with the next line of input.
            INPUT = get_input()
