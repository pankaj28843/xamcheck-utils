# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from xamcheck.utils.words_comparision import OrderedSet

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

    def test_discard(self):
        new_obj = object()
        another_object = object()
        another_objectx = another_object
        ordered_set = OrderedSet(['key', 1, '123', new_obj])
        ordered_set.add(another_object)

        ordered_set.discard(another_objectx)
        self.assertEqual(len(ordered_set), 4)

        ordered_set.discard(1)
        self.assertEqual(len(ordered_set), 3)

        ordered_set.discard(another_object)
        self.assertEqual(len(ordered_set), 3)

        ordered_set.discard(new_obj)
        self.assertEqual(len(ordered_set), 2)

        ordered_set.discard('123')
        self.assertEqual(len(ordered_set), 1)

        ordered_set.discard('KEY')
        self.assertEqual(len(ordered_set), 1)

        ordered_set.discard('key')
        self.assertEqual(len(ordered_set), 0)

    def test_equal(self):
        new_obj = object()
        another_object = object()
        ordered_set = OrderedSet(['key', 1, '123', new_obj, another_object])
        another_ordered_set = OrderedSet(['key', 1, '123', new_obj])
        other_ordered_set = OrderedSet(
            ['key', 1, '123', new_obj, another_object])

        ordered_set.__eq__(other_ordered_set)
        self.assertEqual(set(ordered_set), set(other_ordered_set))

        ordered_set.__eq__(another_ordered_set)
        set(ordered_set) != set(another_ordered_set)

    def test_pop(self):
        new_obj = object()
        ordered_set = OrderedSet(['key', 1, '123', new_obj])

        ordered_set.pop()
        self.assertEqual(len(ordered_set), 3)

        ordered_set.pop()
        self.assertEqual(len(ordered_set), 2)

        ordered_set.pop()
        self.assertEqual(len(ordered_set), 1)

        ordered_set.pop()
        self.assertEqual(len(ordered_set), 0)

    def test_contains(self):

        new_obj = object()
        ordered_set = OrderedSet(['key', 1, '123', new_obj])
        items = (
            ('key', True),
            ('2', False),
            ('123', True),
            (2, False),
            (new_obj, True),

        )

        for value, output in items:
            self.check_output(ordered_set.__contains__, output, value)
