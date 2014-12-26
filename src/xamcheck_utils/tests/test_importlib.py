from __future__ import unicode_literals

# Standard Library
from collections import OrderedDict
from unittest import TestCase

# Xamcheck-Utils Stuff
from xamcheck_utils.importlib import import_from_string


class TestUtilsimportlib(TestCase):

    def test_import_from_string(self):
        items = (
            ('collections.OrderedDict', OrderedDict),
            ('unittest.TestCase', TestCase),
        )
        for value, output in items:

            self.assertEqual(import_from_string(value), output)
        items = (
            ('colections_foobar_mo_random.OderedDict'),
        )
        for value in items:
            with self.assertRaises(ImportError):
                import_from_string(value)

        items = (
            ('collections.OderedDic_random_thing_from_cloudt'),
        )
        for value in items:
            with self.assertRaises(AttributeError):
                import_from_string(value)
