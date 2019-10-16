def alphanumeric(s):
    return all([x.isalpha() or x.isdigit() for x in s])