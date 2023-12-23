"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """Creates a words list from provided file and serves random words
    to the user.

    Attributes
    ----------------
    words: list
        List of words parsed from file
    path: str
        path of file to read

        >>> wf = WordFinder('words.txt')
        235886 words read

        >>> wf.random() in wf.words
        True

    """

    def __init__(self, path):
        self.words = self.parse_file(path)
        self.path = path
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"WordFinder(path={self.path})"

    def parse_file(self, path):
        """Opens file at specified path. Returns a list where each line
        in provided file is a list item."""
        with open(path, "r") as file:
            return [line.strip() for line in file]

    def random(self):
        """Returns random word from words list"""
        return choice(self.words)
