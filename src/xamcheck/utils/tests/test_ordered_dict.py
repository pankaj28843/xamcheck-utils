# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from xamcheck.utils.ordered_set import OrderedSet

from .base import TestCase


class TestOrderedSet(TestCase):

    def test_add(self):
        ordered_set = OrderedSet()

        ordered_set.add("something")
        self.assertEqual(len(ordered_set), 1)

        ordered_set.add("something")
        self.assertEqual(len(ordered_set), 1)

        ordered_set.add(1)
        self.assertEqual(len(ordered_set), 2)

        new_obj = object()
        ordered_set.add(new_obj)
        self.assertEqual(len(ordered_set), 3)

        another_object = object()
        ordered_set.add(another_object)
        self.assertEqual(len(ordered_set), 4)

        ordered_set.add(another_object)
        self.assertEqual(len(ordered_set), 4)
