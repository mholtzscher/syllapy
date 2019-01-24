"""Tests for `syllapy` package."""

from string import punctuation

import syllapy


def test_simple():
    """Simple Test."""
    assert syllapy.count("dog!!!!!") == 1


def test_none():
    """Testing passing `None` type."""
    assert syllapy.count(None) == 0


def test_bool():
    """Testing passing `bool` type."""
    assert syllapy.count(True) == 0


def test_int():
    """Testing passing `None` type."""
    assert syllapy.count(2) == 0


def test_empty():
    """Test empty string"""
    assert syllapy.count("") == 0


def test_space():
    """Testing passing space"""
    assert syllapy.count(" ") == 0


def test_punctuation_only():
    """Testing punctuation only"""
    for punct in punctuation:
        assert syllapy.count(punct) == 0


def test_not_in_dict():
    """Test word not in known dataset"""
    assert syllapy.count("ostentatious") == 4


def test_in_dict():
    """Test words in known dataset"""
    assert syllapy.count("because") == 2
    assert syllapy.count("woman") == 2
    assert syllapy.count("international") == 5


def test_case_insensitive():
    """Test words changing capitalization"""
    assert syllapy.count("Norway") == 2
    assert syllapy.count("norway") == 2
    assert syllapy.count("Ohio") == 3
    assert syllapy.count("ohio") == 3
