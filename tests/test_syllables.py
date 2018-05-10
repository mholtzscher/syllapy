import spacy
import pytest


@pytest.fixture(scope='function')
def nlp():
    return spacy.load('en')


def test_simple(nlp):
    doc = nlp("sample")
    assert doc