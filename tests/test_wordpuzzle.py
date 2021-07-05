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
from hypothesis.strategies import integers, text

from lib.filters import is_valid_letters, is_valid_size, is_valid_word


@given(integers(min_value=1, max_value=9))
def test_valid_size(size):
    assert is_valid_size(size)


@given(integers(min_value=10))
def test_size_too_large(size):
    assert not is_valid_size(size)


@given(integers(max_value=0))
def test_size_to_small(size):
    assert not is_valid_size(size)


@given(text(min_size=9, max_size=9, alphabet=list(ascii_lowercase)))
def test_valid_letters(letters):
    assert is_valid_letters(letters)


@given(text(min_size=10, max_size=30, alphabet=list(ascii_lowercase)))
def test_too_many_letters(letters):
    assert not is_valid_letters(letters)


@given(text(max_size=9, alphabet=list(ascii_uppercase)))
def test_not_valid_letters(letters):
    assert not is_valid_letters(letters)


LETTERS = list('cadevrsoi')


class TestWordPuzzle(unittest.TestCase):
    """ Test word puzzle utility functions. """

    def setUp(self):
        self.letters = LETTERS
        self.size = 4

    def test_not_valid_word_too_short(self):
        word = list('ice')
        assert not is_valid_word(self.size, self.letters, word)
        assert self.letters == LETTERS

    def test_not_valid_word_too_long(self):
        word = list('adevcrsoia')
        assert not is_valid_word(self.size, self.letters, word)
        assert self.letters == LETTERS

    def test_valid_word(self):
        word = list('voice')
        assert is_valid_word(self.size, self.letters, word)
        assert self.letters == LETTERS

    def test_not_valid_word(self):
        word = list('voicedx')
        assert not is_valid_word(self.size, self.letters, word)
        assert self.letters == LETTERS
