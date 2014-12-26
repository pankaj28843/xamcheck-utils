# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Xamcheck-Utils Stuff
from xamcheck_utils import func

from .base import TestCase


class TestUtilsFunc(TestCase):

    def test_percent(self):
        f = func.percent
        items = (
            (12, 'a', 0),
            (30, '110', 27.27),
            (30, 110, 27.27),

        )

        for value1, value2, output in items:
            self.check_output(f, output, value1, value2)

    def test_to_alphanumneric_str(self):
        f = func.to_alphanumneric_str
        items = (
            ('Python Code', 'pythoncode'),
            ('Python_Code', 'pythoncode'),
            ('Python_Code123', 'pythoncode123'),
            ('Python code', 'pythoncode'),

        )

        for value, output in items:
            self.check_output(f, output, value)

    def test_drange(self):
        f = func.drange
        items = (
            ((1, 2, 0.25), [1, 1.25, 1.5, 1.75]),
        )

        for (start, stop, step), output in items:
            self.assertEqual(list(f(start, stop, step)), output)
