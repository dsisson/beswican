"""
    This example app was inspired by Rob van der Leeks article:
    https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b
"""

import random
import beswican.data.phrase_components as parts


def sample(data, length=1):
    """
        Generate a random sample from the population `data` of length `length`.

        :param data: iterable
        :param length: int, length of result set
        :return result: either a list of str or a str
    """
    result = random.sample(data, length)
    if length == 1:
        return result[0]
    return result


def generate_phrase():
    """
        Generate a buzzword phrase from the random sample of the phrase component data.

        :return: str, title-cased phrase
    """
    buzz_terms = sample(parts.noun_phrases, 2)
    phrase = ' '.join([
                        sample(parts.adjectives),
                        buzz_terms[0],
                        sample(parts.adverbs),
                        sample(parts.verbs),
                        buzz_terms[1]
                      ])
    return phrase.title()


if __name__ == "__main__":
    print(generate_phrase())