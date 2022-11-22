
"""
An attempt to find the shortest code to reverse a string
"""

def reverse_sentence(word):
    """
    Reverses a sentence or word.
    :param word: str
    :return: str
    """
    return (''.join(list((word)[::-1])))

def reverse_sentence_shortest(word):
    """
    Reverses a sentence or word.
    :param word: str
    :return: str
    """
    return word[::-1]
