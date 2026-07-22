"""Library: Solve 9 Letter Word Puzzle."""

from library.domain import Puzzle


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
    try:
        Puzzle(letters=letters, min_size=4)
        return True
    except ValueError:
        return False


def is_valid_word(size: int, letters: list[str], word: str) -> bool:
    """Check that a dictionary word only contains valid letters
    and is of the correct size.

    The mandatory character is chosen as the first letter in the list of
    letters argument.

    Parameters
    ----------

    size : int
        minimum word size
    letters : list[str]
        the letters that words can be made from
    word : str
        the dictionary word to check

    Returns
    -------

    bool
        true if word is valid, false otherwise
    """
    try:
        # Join letters if passed as a list
        letters_str = "".join(letters)
        puzzle = Puzzle(letters=letters_str, min_size=size)
        return puzzle.matches(word)
    except ValueError:
        return False
