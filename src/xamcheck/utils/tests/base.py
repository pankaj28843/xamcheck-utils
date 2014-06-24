# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase as OriginalTestCase


class TestCase(OriginalTestCase):

    def check_output(self, function, value, output=None):
        """
        Check that function(value) equals output.  If output is None,
        check that function(value) equals value.
        """
        if output is None:
            output = value
        self.assertEqual(function(value), output)
