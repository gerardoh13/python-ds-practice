def to_dict(num):
    """returns a dictionary of digit frequency."""
    num_dict = {}
    for char in str(num):
        if char in num_dict:
            num_dict[char] += 1
        else:
            num_dict[char] = 1
    return num_dict


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    num1_dict = to_dict(num1)
    num2_dict = to_dict(num2)
    return num1_dict == num2_dict
