import syllapy


def test_simple():
    assert 1 == syllapy.count("dog!!!!!")


def test_none():
    assert 0 == syllapy.count(None)


def test_empty():
    assert 0 == syllapy.count("")


def test_space():
    assert 0 == syllapy.count(" ")


def test_punctuation_only():
    assert 0 == syllapy.count(",")
