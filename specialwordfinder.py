"""Special Word Finder"""
from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """Creates a list of words from a file and serves a random word
    to the user.

    Ignores any line with # Comments or empty lines to ensure they
    don't end up in the words list.

    Attributes
    ----------------
    words: list
        List of words parsed from file
    path: str
        path of file to read

        >>> swf = SpecialWordFinder('common_words.txt')
        30 words read

        >>> swf.random().strip() != ''
        True

        >>> swf.random() in swf.words
        True

        >>> swf.random().startswith('#')
        False
    """

    def __repr__(self):
        return f"SpecialWordFinder(path={self.path})"

    def parse_file(self, path):
        """Opens file at specified path. Returns a list where each line
        in provided file is a list item, ignoring empty lines or # Comments"""
        with open(path, "r") as file:
            return [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]
