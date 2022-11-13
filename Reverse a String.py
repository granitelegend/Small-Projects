
def reverse_string(word):
    """
    Reverses string that is input in function.
    :param word:
    :return: str
    """

    word = reversed(list(word))
    reverse_word = ''

    for x in word:
        reverse_word += x

    return reverse_word
