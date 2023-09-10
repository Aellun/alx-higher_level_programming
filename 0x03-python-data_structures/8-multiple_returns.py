#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple having the len of the sentence and its first char.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple having two elements:
            - The len of the sentence and.
            - The first char of the sentence.
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
