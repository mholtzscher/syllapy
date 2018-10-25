import syllapy
import pytest


def test_number_in_word():
    with pytest.raises(ValueError) as e:
        syllapy.count("d0g")


def test_number_start_word():
    with pytest.raises(ValueError) as e:
        syllapy.count("4dog")


def test_number_end_word():
    with pytest.raises(ValueError) as e:
        syllapy.count("dog123")
