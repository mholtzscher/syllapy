"""Loads reference data to memory."""

import csv
from importlib.resources import files


def load_dict() -> dict:
    """
    Loads reference data to dictionary.
    :return: dictionary of the syllable reference data
    """
    words = {}
    text = files("syllapy").joinpath("data.csv").read_text(encoding="utf-8")
    reader = csv.reader(text.splitlines())
    for row in reader:
        words[row[0]] = int(row[1])
    return words
