#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `syllapy` package."""

from string import punctuation

import syllapy


def test_simple():
    assert 1 == syllapy.count("dog!!!!!")


def test_none():
    assert 0 == syllapy.count(None)


def test_bool():
    assert 0 == syllapy.count(True)


def test_int():
    assert 0 == syllapy.count(2)


def test_empty():
    assert 0 == syllapy.count("")


def test_space():
    assert 0 == syllapy.count(" ")


def test_punctuation_only():
    for p in punctuation:
        assert 0 == syllapy.count(p)


def test_not_in_dict():
    assert 4 == syllapy.count("ostentatious")


def test_in_dict():
    assert 2 == syllapy.count("because")
    assert 2 == syllapy.count("woman")
    assert 5 == syllapy.count("international")


def test_case_insensitive():
    assert 2 == syllapy.count("Norway")
    assert 2 == syllapy.count("norway")
    assert 3 == syllapy.count("Ohio")
    assert 3 == syllapy.count("ohio")
