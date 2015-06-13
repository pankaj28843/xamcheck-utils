from __future__ import absolute_import

from importlib import import_module


def import_from_string(s):
    """ Imports the method specified after the last period in
        the string.
    >>> from collections import deque
    >>> import_from_string('collections.deque') == deque
    True
    """
    # grab the classname/function name off of the string
    package, attrib = s.rsplit('.', 1)

    # dynamically import the module
    module = import_module(package)

    # pull the class/function off the module and return
    return getattr(module, attrib)
