#!/usr/bin/env python
# coding: utf-8
# pylint: disable=C0111
# pylint: disable=R0904
"""
Test wordpuzzle is_valid method on basic inputs.
"""

import unittest
from wordpuzzle.wordpuzzle import is_valid


class TestWordPuzzle(unittest.TestCase):
    """ Tests is_valid function. """

    def setUp(self):
        self.letters = list('adevcrsoi')
        self.mandatory = 'c'
        self.size = 4

    def test_too_short(self):
        word = list('ice')
        self.assertFalse(is_valid(self.size, self.mandatory, self.letters,
                                  word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_too_long(self):
        word = list('adevcrsoia')
        self.assertFalse(is_valid(self.size, self.mandatory, self.letters,
                                  word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_valid(self):
        word = list('voice')
        self.assertTrue(is_valid(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_not_valid(self):
        word = list('voicedx')
        self.assertFalse(is_valid(self.size, self.mandatory, self.letters,
                                  word))
        self.assertEqual(self.letters, list('adevcrsoi'))
