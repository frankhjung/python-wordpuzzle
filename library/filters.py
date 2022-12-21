#!/usr/bin/env python3
"""
Library: Solve 9 Letter Word Puzzle.
"""


def is_valid_letters(letters: str) -> bool:
    """Must have 9 alphabetic, lowercase characters.

    Parameters

    letters : str
        the letters that words can be made from

    Returns

    bool
        true if letters are lowercase, false otherwise
    """
    return len(letters) == 9 and letters.isalpha() and letters.islower()


def is_valid_word(size: int, letters: list[str], word: str) -> bool:
    """Check that a dictionary word only contains valid letters
    and is of the correct size.

    The mandatory character is chosen as the first letter in     the
    list of letters argument.

    Parameters

    size : int
        minimum word size
    letters : str
        the letters that words can be made from
    word : str
        the dictionary word to check

    Returns

    bool
        true if word is valid, false otherwise
    """
    # word of the correct size
    if not size <= len(word) < 9:
        return False

    # mandatory letter must be in word
    if letters[0] not in word:
        return False

    # test all letters in word are valid
    working = letters[:]  # deep copy of letters
    result = True  # default if loop completes
    for letter in word:
        if letter in working:
            working.remove(letter)
        else:
            result = False
    return result
