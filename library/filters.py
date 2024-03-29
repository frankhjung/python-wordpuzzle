#!/usr/bin/env python3
"""
Library: Solve 9 Letter Word Puzzle.
"""

from collections import Counter
from re import match


def is_valid_letters(letters: str) -> bool:
    """Must have 9 alphabetic, lowercase characters.

    Parameters
    ----------

    letters : str
        the letters that words can be made from

    Returns
    -------

    bool
        true if letters are lowercase, false otherwise
    """
    return bool(match(r"^[a-z]{9}$", letters))


def is_valid_word(size: int, letters: list[str], word: str) -> bool:
    """Check that a dictionary word only contains valid letters
    and is of the correct size.

    The mandatory character is chosen as the first letter in the list of
    letters argument.

    Parameters
    ----------

    size : int
        minimum word size
    letters : str
        the letters that words can be made from
    word : str
        the dictionary word to check

    Returns
    -------

    bool
        true if word is valid, false otherwise
    """
    # word of the correct size
    if not size <= len(word) <= 9:
        return False

    # mandatory letter must be in word
    if letters[0] not in word:
        return False

    # check if all letters in the word can be formed from the letters list
    letter_counts = Counter(letters)
    word_counts = Counter(word)
    return all(word_counts[letter] <= letter_counts[letter] for letter in word_counts)
