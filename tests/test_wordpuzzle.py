#!/usr/bin/env python3
# pylint: disable=C0111
# pylint: disable=R0801
# pylint: disable=R0904
"""
Test word puzzle validation functions.
"""

from string import ascii_lowercase, printable

from hypothesis import given
from hypothesis.strategies import permutations, text

from library.filters import is_valid_letters, is_valid_word

ALPHABET = list(ascii_lowercase)
LETTERS = list("cadevrsoi")
MANDATORY = LETTERS[0]
SIZE = 4
BAD_LETTERS = list(set(ALPHABET).difference(set(LETTERS)))


@given(text(min_size=1, max_size=SIZE - 1, alphabet=list(ascii_lowercase)))
def test_too_few_letters(letters: str) -> None:
    assert not is_valid_letters(letters)


@given(text(min_size=9, max_size=9, alphabet=list(ascii_lowercase)))
def test_max_valid_letters(letters: str) -> None:
    assert is_valid_letters(letters)


@given(text(min_size=10, max_size=30, alphabet=list(ascii_lowercase)))
def test_too_many_letters(letters: str) -> None:
    assert not is_valid_letters(letters)


@given(text(min_size=8, max_size=8, alphabet=list(printable)))
def test_not_valid_letters_printables(letters: str) -> None:
    assert not is_valid_letters(MANDATORY.upper() + letters)


@given(text(min_size=8, max_size=8, alphabet=list(LETTERS)))
def test_not_valid_letters_mixedcase(letters: str) -> None:
    assert not is_valid_letters(MANDATORY.upper() + letters)


@given(text(min_size=1, max_size=SIZE - 1, alphabet=LETTERS))
def test_not_valid_word_too_short(word: str) -> None:
    assert not is_valid_word(SIZE, LETTERS, word)


@given(text(min_size=9, alphabet=LETTERS))
def test_not_valid_word_too_long(word: str) -> None:
    assert not is_valid_word(SIZE, LETTERS, word)


@given(permutations(LETTERS))
def test_max_valid_word(word: str) -> None:
    assert is_valid_word(SIZE, LETTERS, word)


@given(text(min_size=SIZE, alphabet=BAD_LETTERS))
def test_not_valid_words(word: str) -> None:
    assert not is_valid_word(SIZE, LETTERS, word)
