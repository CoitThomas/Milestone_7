"""Take in a string, reverse it, and return the result."""
import timeit
from get_input import get_input

def easy_way(a_string):
    """Reverse a string in an optimal manner."""
    return a_string[-1:-(len(a_string)+1):-1]

def hard_way(a_string):
    """Reverse a string without utilizing builtins, string functions, or
    list functions with the exception of list().
    """
    chars = list(a_string)
    chars = reverse(chars)
    return string(chars)

def reverse(a_list):
    """Reverse the order of items in a given list and return it."""
    front = 0
    back = len(a_list)-1
    while front < back:
        temp = a_list[front]
        a_list[front] = a_list[back]
        a_list[back] = temp
        front = front + 1
        back = back - 1
    return a_list

def string(a_list):
    """Convert a list into a string and return it."""
    new_string = ''
    for item in a_list:
        new_string = new_string + item
    return new_string

if __name__ == "__main__":
    INPUT = get_input()

    START_TIME = timeit.time.clock()
    print "Easy way: %s" % easy_way(INPUT)
    STOP_TIME = timeit.time.clock()
    print "Run time: %f seconds." % (STOP_TIME - START_TIME)

    START_TIME = timeit.time.clock()
    print "Hard way: %s" % hard_way(INPUT)
    STOP_TIME = timeit.time.clock()
    print "Run time: %f seconds." % (STOP_TIME - START_TIME)
