import pytest

from library.domain import Puzzle, solve


def test_puzzle_valid():
    p = Puzzle(letters="cadevrsoi", min_size=4)
    assert p.mandatory == "c"
    assert p.all_letters == "cadevrsoi"
    assert p.min_size == 4


def test_puzzle_invalid_length():
    with pytest.raises(ValueError, match="exactly 9 lowercase alphabetic letters"):
        Puzzle(letters="abc", min_size=4)


def test_puzzle_invalid_size():
    with pytest.raises(ValueError, match="between 1 and 9"):
        Puzzle(letters="cadevrsoi", min_size=10)


def test_solve_simple():
    p = Puzzle(letters="cadevrsoi", min_size=4)
    dictionary = ["codrives", "apple", "cat", "covaried"]
    results = list(solve(p, dictionary))
    assert "codrives" in results
    assert "covaried" in results
    assert "apple" not in results  # No 'c'
    assert "cat" not in results  # Too short
