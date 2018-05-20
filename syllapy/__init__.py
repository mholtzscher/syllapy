# coding: utf8
from .data_loader import load_dict

word_dict = load_dict()


def count(word):
    word = word.strip().lower()
    if word in word_dict:
        return word_dict[word]
    return _syllables(word)


def _syllables(token):
    syll_count = 0
    vowels = 'aeiouy'
    word = token.text.lower().strip(".:;?!")
    if word[0] in vowels:
        syll_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syll_count += 1
    if word.endswith('e'):
        syll_count -= 1
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        syll_count += 1
    if syll_count == 0:
        syll_count += 1
    return syll_count
