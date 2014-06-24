# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from xamcheck.utils import text


class TestUtilsText(TestCase):

    def check_output(self, function, value, output=None):
        """
        Check that function(value) equals output.  If output is None,
        check that function(value) equals value.
        """
        if output is None:
            output = value
        self.assertEqual(function(value), output)

    def test_unicodify(self):
        f = text.unicodify
        items = (
            ('&', '&amp;'),
            ('<', '&lt;'),
            ('>', '&gt;'),
            ('"', '&quot;'),
            ("'", '&#39;'),
        )

        for value, output in items:
            self.check_output(f, value, output)

    def test_remove_spaces(self):
        f = text.remove_spaces
        items = (
            ('new word', 'newword'),
            ('new word ', 'newword'),
            ('new word\n\rlol', 'newwordlol'),
        )

        for value, output in items:
            self.check_output(f, value, output)

    def test_fix_student_name(self):
        f = text.fix_student_name
        items = (
            ("p v r reddy", "P. V. R. Reddy"),
            ("p v r redd", "P. V. R. Redd"),
            ("pankaj    singh", "Pankaj Singh"),
            ("ram\n chandra", "Ram Chandra"),
        )

        for value, output in items:
            self.check_output(f, value, output)

    def test_soretd_nicely(self):
        """
        Checking whether the function sorted_nicely works properly
        for different types of test cases
        """

        f = text.sorted_nicely
        items = (
            (['1', '11', '2', '3', '21'], ['1', '2', '3', '11', '21']),
        )

        for value, output in items:
            self.check_output(f, value, output)
