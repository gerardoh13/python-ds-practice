def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ["a","e","i","o","u"]
    vowel_count = {}
    phrase = phrase.lower()
    for char in phrase:
        if char in vowels:
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1
    return vowel_count
