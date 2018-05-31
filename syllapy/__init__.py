# -*- coding: utf-8 -*-

"""Top-level package for SyllaPy."""

__author__ = """Michael Holtzscher"""
__email__ = 'mholtz@protonmail.com'
__version__ = '0.2.0'

import logging
from string import punctuation

from .data_loader import load_dict

log = logging.getLogger(__name__)

# load the known words dictionary
word_dict = load_dict()


def count(word: str) -> int:
    """Returns number of syllables in a word. If the word is None, not a string, or empty then returns 0.
    :rtype: int
    :param word: the word to count syllables for
    :return: the number of syllables in the word
    """
    try:
        word = word.strip().lower().strip(punctuation)
        if len(word) == 0:
            return 0
        if word in word_dict:
            return word_dict[word]
        log.info("'%s' not found in known word list.", word)
        return _syllables(word)
    except AttributeError:
        return 0


def _syllables(word: str) -> int:
    """
    :param word:
    :return:
    """
    syllable_count = 0
    vowels = 'aeiouy'
    if word[0] in vowels:
        syllable_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1
    if word.endswith('e'):
        syllable_count -= 1
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
    return syllable_count
