# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from xamcheck.utils import crypto

from .base import TestCase


class TestUtilsSecure(TestCase):

    def test_hash_string(self):
        f = crypto.hash_string
        items = (
            ('abhyuday', '78b0c82d7c7e4ce0f679541c19f1122ef1bbec657f3b00e34b0b562dca2100abcd8fe70c17adc8477ba7b797053b00f7fc57b82a1465578069300e9f805f292d'),
            ('12345', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79'),
            ('abhyuday12345', '99412cdae9105c1e6796605b8f9ec30be2bbd83587c7c74a5c7d8e34db6cee10bb1f8c7bfd3bdb095f62d7d3491bb465431e4746ebdafdbf2a478a5a9f9555d1'),
        )

        for value, output in items:
            self.check_output(f, output, value)
