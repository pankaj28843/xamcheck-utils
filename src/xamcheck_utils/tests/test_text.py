# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Xamcheck-Utils Stuff
from xamcheck_utils import text

from .base import TestCase


class TestUtilsText(TestCase):

    def test_unicodify(self):
        f = text.unicodify
        items = (
            ('&', '&amp;'),
            ('<', '&lt;'),
            ('>', '&gt;'),
            ('"', '&#34;'),
            ("'", '&#39;'),
        )

        for value, output in items:
            self.check_output(f, output, value)

    def test_remove_spaces(self):
        f = text.remove_spaces
        items = (
            ('new word', 'newword'),
            ('new word ', 'newword'),
            ('new word\n\rlol', 'newwordlol'),
        )

        for value, output in items:
            self.check_output(f, output, value)

    def test_fix_student_name(self):
        f = text.fix_student_name
        items = (
            ("p v r reddy", "P. V. R. Reddy"),
            ("p v r redd", "P. V. R. Redd"),
            ("pankaj    singh", "Pankaj Singh"),
            ("ram\n chandra", "Ram Chandra"),
        )

        for value, output in items:
            self.check_output(f, output, value)

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
            self.check_output(f, output, value)

    def test_fix_name(self):
        f = text.fix_name
        items = (
            ("Mahatma    Gandhi", "Mahatma Gandhi"),
            ("Air-base", "Air - base"),
        )

        for value, output in items:
            self.check_output(f, output, value)
