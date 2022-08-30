def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    char_list = list(s)
    i = 0
    j = len(char_list) - 1
    vowels = set("aeiou")
    while i < j:
        if char_list[i] not in vowels:
            i += 1
        elif char_list[j] not in vowels:
            j -= 1
        else:
            char_list[i], char_list[j] = char_list[j], char_list[i]
            i += 1
            j -= 1
    return "".join(char_list)