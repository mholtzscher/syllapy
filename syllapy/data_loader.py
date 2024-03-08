"""Loads reference data to memory."""

import csv
import importlib.resources


def load_dict() -> dict:
    """
    Loads reference data to dictionary.
    :return: dictionary of the syllable reference data
    """
    file_name = "data.csv"
    file_path = importlib.resources.files("syllapy").joinpath(file_name)
    words = {}

    with open(file_path, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            words[row[0]] = int(row[1])
    return words
