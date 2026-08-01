"""Top-level package for SyllaPy."""

__author__ = """Michael Holtzscher"""
__email__ = "mholtz@protonmail.com"

import logging
import re
from importlib.metadata import PackageNotFoundError, version
from string import punctuation

from .data_loader import load_dict

try:
    __version__ = version("syllapy")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

LOGGER = logging.getLogger(__name__)
NUMBERS = re.compile(r"\d")

# load the known words dictionary
WORD_DICT = load_dict()


def count(word: str) -> int:
    """Returns number of syllables in a word.
    If the word is None, not a string, contains invalid chars, or empty then returns 0.
    :rtype: int
    :param word: the word to count syllables for
    :return: the number of syllables in the word
    """
    if not isinstance(word, str):
        LOGGER.debug("'%s' is not a string.", word)
        return 0

    word = word.strip().lower().strip(punctuation)
    if not word:
        LOGGER.debug("'%s' has length of zero after stripping extra chars.", word)
        return 0
    if _contains_numbers(word):
        LOGGER.debug("'%s' contains numbers.", word)
        return 0
    if word in WORD_DICT:
        return WORD_DICT[word]

    LOGGER.debug("'%s' not found in known word list.", word)

    # compound words like self-care
    r = re.match("([^-]+)-(.+)", word)
    if r:
        s1 = count(r.group(1))
        s2 = count(r.group(2))
        LOGGER.debug(
            "'%s' is compound of %s = %s and %s = %s",
            word,
            r.group(1),
            s1,
            r.group(2),
            s2,
        )
        if s1 == 0 or s2 == 0:
            return 0
        return s1 + s2

    return _syllables(word)


def _syllables(word: str) -> int:
    syllable_count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        syllable_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1
    if word.endswith("e"):
        syllable_count -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
    return syllable_count


def _contains_numbers(word: str) -> bool:
    return bool(NUMBERS.search(word))
