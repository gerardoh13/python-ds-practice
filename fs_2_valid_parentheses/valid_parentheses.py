def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # function can accept {}, [], and ()
    parens_ref = '()[]{}'
    stack = []
    for char in parens:
        idx = parens_ref.index(char)
        if idx % 2 == 0:
            stack.append(idx + 1)
        else:
            if not len(stack):
                return False
            elif stack.pop() != idx:
                return False
    return len(stack) == 0