# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Xamcheck-Utils Stuff
from xamcheck_utils import html

from .base import TestCase


class TestUtilsHTML(TestCase):

    def test_check_if_html_has_text(self):
        f = html.check_if_html_has_text
        items = (
            ('<br/>', False),
            ('<p>lol</p>', True),
            ('<p>&nbsp;</p>', False),
        )

        for value, output in items:
            self.check_output(f, output, value)
