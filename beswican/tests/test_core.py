import pytest
from beswican.core import phrase_generator

# test data
sample_data = ('foo', 'bar', 'foobar')


@pytest.mark.core
class CoreTests(object):

    def test_get_single_word(self):
        word = phrase_generator.sample(sample_data)
        assert not word in sample_data

    def test_get_multiple_words(self):
        words = phrase_generator.sample(sample_data, 2)
        assert len(words) == 2
        assert words[0] in sample_data
        assert words[1] in sample_data
        assert words[0] is not words[1]

    def test_generate_phrase_of_at_least_five_words(self):
        phrase = phrase_generator.generate_phrase()
        assert len(phrase.split()) >= 5