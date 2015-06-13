# Standard Library
import re

# Third Party Stuff
from markupsafe import escape


def unicodify(s, strip=True):  # Testcases not written.
    s = escape(s)
    if not (isinstance(s, str) or isinstance(s, unicode)):
        return s
    if isinstance(s, unicode):
        s = s.encode('utf8')
    if strip:
        return s.strip()
    else:
        return s


def number2string(s):
    """ Return string representation of a number.

    Returns as it is, if ValueError is raised.    #this feature not working
    Returns string exponent form for very large numbers.

    >>> number2string(21.3) == '21.3'
    True
    >>> number2string(21) == '21'
    True
    >>> number2string('lol') == 'lol'
    True
    """
    try:
        return '{0:g}'.format(float(s))
    except ValueError:
        return s


def string2float(s):
    """ Returns float value if number passed as string.
    >>> string2float('111.111') == 111.111
    True

    """
    return float(s)


def string2int(s):
    """ Returns integer value if number is passed as string.
    >>> string2int('111.111') == 111
    True
    """
    return int(float(s))

"""Comma seperated strings to list conversion"""


# Don't know exactly what these 2 lines do
REGEX_COMMA_SEPARATED_INT = re.compile(r"^,|,$|\s")
REGEXT_COMMA = re.compile(r",")


def comma_separated_int_to_list(s):
    """ Returns list containing integers if numbers are
        passed as string seperated by commas
    >>> comma_separated_int_to_list('111,12') == [111, 12]
    True
    """
    s = REGEX_COMMA_SEPARATED_INT.sub("", s)
    return map(string2int, filter(len, REGEXT_COMMA.split(s)))


def comma_separated_float_to_list(s):
    """ Returns a list containing float values of the
        numbers passes as string seperated by commas.

    >>> comma_separated_float_to_list('11.1,12') == [11.1, 12.0]
    True
    >>> comma_separated_float_to_list('11,12.1,0.4') == [11.0, 12.1, 0.4]
    True
    """
    s = REGEX_COMMA_SEPARATED_INT.sub("", s)
    return map(string2float, filter(len, REGEXT_COMMA.split(s)))


def comma_separated_str_to_list(s):
    """Separetes string based on commas and stores each
        string as different strings in a list.

    >>> comma_separated_str_to_list('Ram,Laxman') == ['Ram', 'Laxman']
    True
    >>> comma_separated_str_to_list('Ram,laxman') == ['Ram', 'laxman']
    True
    >>> comma_separated_str_to_list('111,112') == ['111', '112']
    True
    """

    s = REGEX_COMMA_SEPARATED_INT.sub("", s)
    return map(unicodify, filter(len, REGEXT_COMMA.split(s)))


def percent(a, b, r=2):
    try:
        return round(float(a) / float(b) * 100, r)
    except:
        return 0
