# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Standard Library
import itertools
import re

# Third Party Stuff
from markupsafe import escape


def unicodify(s, strip=True):
    """ Encodes given string to unicode
    >>> unicodify(u'\u00c3')
    '\\xc3\\x83'
    """

    s = escape(s)
    if not (isinstance(s, str) or isinstance(s, unicode)):
        return s
    if isinstance(s, unicode):
        s = s.encode('utf8')
    if strip:
        return s.strip()
    else:
        return s


def remove_spaces(s):
    """ Removes spaces from a given string using regular expressions

    here is an extra line
    >>> remove_spaces("   foo  \\n bar \\t moo")
    u'foobarmoo'

    yet another line then we will add a doctest

    >>> remove_spaces("foo lo bar         ")
    u'foolobar'
    """
    return ''.join(re.split(r'\s', s))


def fix_name(name):
    """ Removes unwanted spaces in a name
    >>> fix_name("hello-world")
    u'hello - world'
    >>> fix_name("hello          world")
    u'hello world'
    """
    name = re.sub("\s*-\s*", " - ", name)
    name = re.sub("\s+", " ", name)
    return name


def fix_student_name(name):
    """ Fix a student's name
    >>> fix_student_name("p v r reddy")
    u'P. V. R. Reddy'
    """
    name = fix_name(name)
    parts = name.split()
    new_parts = []

    for part in parts:
        if len(part) == 1:
            part = part + '.'
        new_parts.append(part.title())

    name = ' '.join(new_parts)
    name = name
    return name


def sorted_nicely(l):
    """Sort the given list in the way that humans expect.
    >>> sorted_nicely(["Q1", "Q3", "Q2", "Q20", "Q11"])
    [u'Q1', u'Q2', u'Q3', u'Q11', u'Q20']
    """
    l = list(l)

    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)
