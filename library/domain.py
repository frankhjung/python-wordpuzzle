import re
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Puzzle:
    letters: str
    min_size: int
    mandatory: str = field(init=False)
    all_letters: str = field(init=False)
    letter_counts: Counter[str] = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        if not re.match(r"^[a-z]{9}$", self.letters):
            raise ValueError("Puzzle must have exactly 9 lowercase alphabetic letters")
        if not (1 <= self.min_size <= 9):
            raise ValueError("min_size must be between 1 and 9")

        # Use object.__setattr__ because the dataclass is frozen
        object.__setattr__(self, "mandatory", self.letters[0])
        object.__setattr__(self, "all_letters", self.letters)
        object.__setattr__(self, "letter_counts", Counter(self.letters))

    def matches(self, word: str) -> bool:
        """Check if a word satisfies the puzzle constraints."""
        if not (self.min_size <= len(word) <= 9):
            return False
        if self.mandatory not in word:
            return False

        word_counts = Counter(word)
        return all(
            word_counts[char] <= self.letter_counts[char] for char in word_counts
        )


def solve(puzzle: Puzzle, dictionary: Iterable[str]) -> Iterator[str]:
    """Identify valid words from a dictionary that satisfy the puzzle."""
    for word in dictionary:
        if puzzle.matches(word):
            yield word
