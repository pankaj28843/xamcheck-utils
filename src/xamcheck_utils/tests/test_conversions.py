from __future__ import unicode_literals

# Standard Library
from unittest import TestCase

# Xamcheck-Utils Stuff
from xamcheck_utils import conversions


class TestUtilsText(TestCase):

    def check_output(self, function, output=None, *value):
        """
        Check that function(value) equals output.  If output is None,
        check that function(value) equals value.
        """
        if output is None:
            output = None
        self.assertEqual(function(*value), output)

    def test_number2string(self):
        f = conversions.number2string
        items = (
            ('1.11116e+22', '11111555555555555555555'),
            ('11', '11.0'),
            ('0.1', '0.1')
        )

        for output, value in items:
            self.check_output(f, output, value)

    def test_string2float(self):
        f = conversions.string2float
        items = (
            (11.0, "11"),
            (11.11, "11.11"),
        )

        for output, value in items:
            self.check_output(f, output, value)

    def test_string2int(self):
        f = conversions.string2int
        items = (
            (0, '0.12'),

        )

        for output, value in items:
            self.check_output(f, output, value)

    """Now testing comma seperated string to lists conversion"""

    def test_comma_separated_int_to_list(self):
        f = conversions.comma_separated_int_to_list
        items = (
            ([11, 12, 13], '11,12.4,13.5'),
            ([11, 0], '11.3,0.5'),
        )

        for value, output in items:
            self.check_output(f, value, output)

    def test_comma_separated_float_to_list(self):
        """Tests performed in doctests probably no
            other testcases required
        """
        pass

    def test_comma_separated_str_to_list(self):
        """ Tests performed in doctests probably no
            other test cases required.
        """
        pass

    def test_percent(self):
        f = conversions.percent
        items = (
            (1.0, 1, 100),
            (0, 1, 'a'),
        )

        for output, value1, value2 in items:
            self.check_output(f, output, value1, value2)
