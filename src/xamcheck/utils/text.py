# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.utils.html import escape


def unicodify(s, strip=True):
    """
    update this
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
    return ''.join(re.split(r'\s', s))


def fix_name(name):
    name = re.sub("\s*-\s*", " - ", name)
    name = re.sub("\s+", " ", name)
    return name


def fix_student_name(name):
    name = fix_name(name)
    parts = name.split()
    new_parts = []

    for part in parts:
        if len(part) == 1:
            part = part + '.'
        new_parts.append(part.title())

    name = ' '.join(new_parts)
    return name
