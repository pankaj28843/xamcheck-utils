# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from xamcheck.utils.ordered_dict import DefaultOrderedDict

from .base import TestCase


class TestOrderedSet(TestCase):

    def test_getitem(self):
        items = [('yellow', 1), ('blue', 2),
                 ('yellow', 3), ('blue', 4), ('red', 1), (1, 'samsung')]
        default_ordered_dict = DefaultOrderedDict(list)
        for k, v in items:
            default_ordered_dict[k].append(v)

        values = default_ordered_dict.__getitem__('yellow')
        self.assertEqual(values, [1, 3])

        values = default_ordered_dict.__getitem__(1)
        self.assertEqual(values, ['samsung'])
