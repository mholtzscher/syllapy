"""Loads reference data to memory."""
import pkg_resources

import ujson


def load_dict() -> dict:
    """
    Loads reference data to dictionary.
    :return: dictionary of the syllable reference data
    """
    file_name = "data.json"
    file_path = pkg_resources.resource_filename(__name__, file_name)
    with open(file_path) as file:
        words = ujson.load(file)
    return words
