# Standard Library
import hashlib


def hash_string(s):
    return hashlib.sha512(s).hexdigest()
