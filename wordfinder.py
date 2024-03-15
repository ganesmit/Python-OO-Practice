"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Find random words from a dictionary.

    >>> wf = WordFinder("simple.txt")
    3 words

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True"""

    def __init__(self, path):

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Enable to get a list of words"""

        return [w.strip() for w in dict_file]

    def random(self):
        """Get random word"""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """We are never returning blank lines or comments

    >>>swf = SpecialWordFinder("complex.txt")
    3 words

    >>>swf.random() in ["pear", "carrot", "kale"]
    True"""

    def parse(self, dict_file):
        """Get list of words and skip blank lines and comments"""

        return [w.strip() for w in dict_file
                if w.strip and not w.startswith("#")]
