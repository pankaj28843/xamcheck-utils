import re
import itertools


def percent(a, b, r=2):
    try:
        return round(float(a) / float(b) * 100, r)
    except:
        return 0


def to_alphanumneric_str(s):
    return "".join(re.findall("[a-zA-Z0-9]+", s)).lower()


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
