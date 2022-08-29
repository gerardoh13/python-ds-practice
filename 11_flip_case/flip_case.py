def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = []
    for char in phrase:
        if char == to_swap:
            char = char.swapcase()
            lst.append(char)
        elif char == to_swap.swapcase():
            char = char.swapcase()
            lst.append(char)
        else:
            lst.append(char)
    return "".join(lst)
