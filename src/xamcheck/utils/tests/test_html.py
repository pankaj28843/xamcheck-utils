# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from xamcheck.utils import html


class TestUtilsHTML(TestCase):

    def check_output(self, function, value, output=None):
        """
        Check that function(value) equals output.  If output is None,
        check that function(value) equals value.
        """
        if output is None:
            output = value
        self.assertEqual(function(value), output)

    def test_check_if_html_has_text(self):
        f = html.check_if_html_has_text
        items = (
            ('<br/>', False),
            ('<p>lol</p>', True),
            ('<p>&nbsp;</p>', False),
        )

        for value, output in items:
            self.check_output(f, value, output)
