def first_non_repeating_letter(s):
    for x in s:
        if s.lower().count(x.lower()) == 1: return x
    return ''