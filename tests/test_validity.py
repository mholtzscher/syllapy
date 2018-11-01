"""Tests for `syllapy` word validity."""

import syllapy


def test_number_in_word():
    """Test number in word"""
    assert syllapy.count("d0g") == 0


def test_number_start_word():
    """Test number at start of word"""
    assert syllapy.count("4dog") == 0


def test_number_end_word():
    """Test number at end of word"""
    assert syllapy.count("dog123") == 0
