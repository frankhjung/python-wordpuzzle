#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111
# pylint: disable=R0801
# pylint: disable=R0904
"""
Test word puzzle validation functions.
"""

from string import ascii_lowercase, printable

from hypothesis import given
from hypothesis.strategies import integers, text

from lib.filters import is_valid_letters, is_valid_size, is_valid_word

ALPHABET = list(ascii_lowercase)
MANDATORY = 'c'
LETTERS = list('adevrsoi')
SIZE = 4
BAD_LETTERS = list(set(ALPHABET).difference(set(LETTERS)))


@given(integers(min_value=1, max_value=9))
def test_valid_size(size: int) -> None:
    assert is_valid_size(size)


@given(integers(min_value=10))
def test_size_too_large(size: int) -> None:
    assert not is_valid_size(size)


@given(integers(max_value=0))
def test_size_to_small(size: int) -> None:
    assert not is_valid_size(size)


@given(text(min_size=1, max_size=SIZE - 1, alphabet=list(ascii_lowercase)))
def test_too_few_letters(letters: str) -> None:
    assert not is_valid_letters(letters)


@given(text(min_size=9, max_size=9, alphabet=list(ascii_lowercase)))
def test_valid_letters(letters: str) -> None:
    assert is_valid_letters(letters)


@given(text(min_size=10, max_size=30, alphabet=list(ascii_lowercase)))
def test_too_many_letters(letters: str) -> None:
    assert not is_valid_letters(letters)


@given(text(min_size=9, max_size=9, alphabet=list(printable)))
def test_not_valid_letters_printables(letters: str) -> None:
    assert not is_valid_letters(MANDATORY.upper() + letters)


@given(text(min_size=9, max_size=9, alphabet=list(LETTERS)))
def test_not_valid_letters_mixedcase(letters: str) -> None:
    assert not is_valid_letters(MANDATORY.upper() + letters)


@given(text(min_size=1, max_size=SIZE - 1, alphabet=LETTERS))
def test_not_valid_word_too_short(word: str) -> None:
    assert not is_valid_word(SIZE, LETTERS, word)


@given(text(min_size=9, alphabet=LETTERS))
def test_not_valid_word_too_long(word: str) -> None:
    assert not is_valid_word(SIZE, LETTERS, word)


@given(text(min_size=SIZE, max_size=8, alphabet=LETTERS))
def test_valid_words(word: str) -> None:
    assert not is_valid_word(SIZE, LETTERS, MANDATORY + word)


@given(text(min_size=SIZE, alphabet=BAD_LETTERS))
def test_not_valid_words(word: str) -> None:
    assert not is_valid_word(SIZE, LETTERS, word)
