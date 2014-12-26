# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Xamcheck-Utils Stuff
from xamcheck_utils import crypto

from .base import TestCase


class TestCrypto(TestCase):

    def test_hash_string(self):
        function_crypto = crypto.hash_string
        items = (
            ('samsung', '4c5849d848150bbcbfdd69b5dab68db028c1ce182c7d194e8d4d0cd40052ef6e04a2154eca4fb5a8514acf1714660f9ac186d552f1b33d6ae131b74b3370b2a0'),
            ('12345', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79'),
            ('samsung12345', '6e50ef68b36c4206d9f122193f4c622faadd1c4ca8874df3a0cc5e4647e63eb7ee2d88752d25b4801f2bc48c7b4e70a6420949f4fe4c145d9afd5f627cb08507'),
        )

        for value, output in items:
            self.check_output(function_crypto, output, value)
