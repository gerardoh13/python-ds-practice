def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    words_list = phrase.split()
    result = []
    for word in words_list:
        result.append(word[0].upper() + word[1::])
    return " ".join(result)
