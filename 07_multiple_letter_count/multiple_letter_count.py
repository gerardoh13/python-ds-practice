def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    word_count_dict = {}
    for char in phrase:
        if char in word_count_dict:
            word_count_dict[char] += 1
        else:
            word_count_dict[char] =1
    return word_count_dict