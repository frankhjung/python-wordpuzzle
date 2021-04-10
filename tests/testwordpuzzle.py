#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111
# pylint: disable=R0801
# pylint: disable=R0904
"""
Test word puzzle validation functions.
"""

import unittest
from string import ascii_lowercase, ascii_uppercase

from hypothesis import given
from hypothesis.strategies import characters, integers, text

import utils.filters as utils


class TestWordPuzzle(unittest.TestCase):
    """ Test word puzzle utility functions. """

    def setUp(self):
        self.letters = list('adevcrsoi')
        self.mandatory = 'c'
        self.size = 4

    def test_not_valid_word_too_short(self):
        word = list('ice')
        self.assertFalse(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_not_valid_word_too_long(self):
        word = list('adevcrsoia')
        self.assertFalse(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_valid_word(self):
        word = list('voice')
        self.assertTrue(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    def test_not_valid_word(self):
        word = list('voicedx')
        self.assertFalse(
            utils.is_valid_word(self.size, self.mandatory, self.letters, word))
        self.assertEqual(self.letters, list('adevcrsoi'))

    @given(integers(min_value=1, max_value=9))
    def test_valid_size(self, size):
        self.assertTrue(utils.is_valid_size(size))

    @given(integers(min_value=10))
    def test_not_valid_size(self, size):
        self.assertFalse(utils.is_valid_size(size))

    @given(characters(whitelist_categories=(['Ll'])))
    def test_valid_mandatory(self, mandatory):
        self.assertTrue(utils.is_valid_mandatory(mandatory))

    @given(characters(whitelist_categories=(['Lu'])))
    def test_not_valid_mandatory(self, mandatory):
        self.assertFalse(utils.is_valid_mandatory(mandatory))

    @given(text(min_size=9, max_size=9, alphabet=list(ascii_lowercase)))
    def test_valid_letters(self, letters):
        self.assertTrue(utils.is_valid_letters(letters))

    @given(text(max_size=9, alphabet=list(ascii_uppercase)))
    def test_not_valid_letters(self, letters):
        self.assertFalse(utils.is_valid_letters(letters))
