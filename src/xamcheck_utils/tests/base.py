# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Standard Library
from unittest import TestCase as OriginalTestCase


class TestCase(OriginalTestCase):

    def check_output(self, function, output=None, *value):
        """
        Check that function(value) equals output.  If output is None,
        check that function(value) equals value.
        """
        if output is None:
            output = None
        self.assertEqual(function(*value), output)
