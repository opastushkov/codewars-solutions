from collections import Counter

def scramble(s1, s2):
    return Counter(s1) & Counter(s2) == Counter(s2)