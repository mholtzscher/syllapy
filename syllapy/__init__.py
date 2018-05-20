# coding: utf8
from string import punctuation

from .data_loader import load_dict

word_dict = load_dict()


def count(word):
    if word is None:
        return 0
    word = word.strip().lower().strip(punctuation)
    if len(word) == 0:
        return 0
    if word in word_dict:
        return word_dict[word]
    return _syllables(word)


def _syllables(word):
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
