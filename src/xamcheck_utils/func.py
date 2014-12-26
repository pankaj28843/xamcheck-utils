# Standard Library
import itertools
import re


def percent(a, b, r=2):
    try:
        return round(float(a) / float(b) * 100, r)
    except:
        return 0


def to_alphanumneric_str(s):
    return "".join(re.findall("[a-zA-Z0-9]+", s)).lower()


def drange(start, stop, step, include_stop=False):
    r = start
    if include_stop is True:
        while r <= stop:
            yield r
            r += step
    else:
        while r < stop:
            yield r
            r += step
