#!/usr/bin/env python
# coding: utf-8
# pylint: disable=C0111
# pylint: disable=R0801
# pylint: disable=R0904
"""
Test word puzzle validation functions.
"""

import unittest
import utils.filters as utils


class TestWordPuzzle(unittest.TestCase):
    """ Test word puzzle utility functions. """

    def setUp(self):
        self.letters = list('adevcrsoi')
        self.mandatory = 'c'
        self.size = 4

    def test_too_short(self):
        word = list('ice')
        self.assertFalse(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_too_long(self):
        word = list('adevcrsoia')
        self.assertFalse(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_valid(self):
        word = list('voice')
        self.assertTrue(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_not_valid(self):
        word = list('voicedx')
        self.assertFalse(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))
