import syllapy


def test_number_in_word():
    assert 0 == syllapy.count("d0g")


def test_number_start_word():
    assert 0 == syllapy.count("4dog")


def test_number_end_word():
    assert 0 == syllapy.count("dog123")
