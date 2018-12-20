# -*- coding: utf-8 -*-

"""Top-level package for SyllaPy."""

__author__ = """Michael Holtzscher"""
__email__ = "mholtz@protonmail.com"
__version__ = "0.7.0"

import logging
import re
from string import punctuation

from .data_loader import load_dict

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
    try:
        word = word.strip().lower().strip(punctuation)
        if not word:
            LOGGER.debug(f"'{word}' has length of zero after stripping extra chars.")
            return 0
        if _contains_numbers(word):
            LOGGER.debug(f"'{word}' contains numbers.")
            return 0
        if word in WORD_DICT:
            return WORD_DICT[word]
        LOGGER.debug(f"'{word}' not found in known word list.")
        return _syllables(word)
    except AttributeError:
        LOGGER.debug(f"'{word}' raised an AttributeError.")
        return 0


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
