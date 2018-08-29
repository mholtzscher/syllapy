"""Loads reference data to memory."""
import csv

import pkg_resources


def load_dict() -> dict:
    """
    Loads reference data to dictionary.
    :return: dictionary of the syllable reference data
    """
    file_name = "data.csv"
    file_path = pkg_resources.resource_filename(__name__, file_name)
    words = {}
    with open(file_path, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            words[row[0]] = int(row[1])
    return words
