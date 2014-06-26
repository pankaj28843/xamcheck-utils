from django.conf import settings
from django.utils.importlib import import_module


def import_from_string(s):
    # grab the classname/function name off of the string
    package, attrib = s.rsplit('.', 1)

    # dynamically import the module
    module = import_module(package)

    # pull the class/function off the module and return
    return getattr(module, attrib)
