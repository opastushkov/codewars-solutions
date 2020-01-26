def valid_parentheses(s):
    l_p = list()
    for x in s:
        try:
            if x == '(': l_p.append('(')
            elif x == ')': l_p.remove('(')
        except ValueError: return False
    return True if len(l_p) == 0 else False