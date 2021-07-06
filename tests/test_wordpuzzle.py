#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111
# pylint: disable=R0801
# pylint: disable=R0904
"""
Test word puzzle validation functions.
"""

from string import ascii_lowercase, ascii_uppercase

from hypothesis import given
from hypothesis.strategies import integers, text

from lib.filters import is_valid_letters, is_valid_size, is_valid_word

LETTERS = list('cadevrsoi')
SIZE = 4


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


def test_not_valid_word_too_short():
    assert not is_valid_word(SIZE, LETTERS, "ice")


def test_not_valid_word_too_long():
    assert not is_valid_word(SIZE, LETTERS, "adevcrsoia")


def test_valid_word():
    assert is_valid_word(SIZE, LETTERS, "voice")


def test_not_valid_word():
    assert not is_valid_word(SIZE, LETTERS, "voicedx")
