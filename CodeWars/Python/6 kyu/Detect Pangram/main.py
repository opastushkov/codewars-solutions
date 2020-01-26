def is_pangram(s):
    return set('abcdefghijklmnopqrstyvwxyz') < set(s.lower())