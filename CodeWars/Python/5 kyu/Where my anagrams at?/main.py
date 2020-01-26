from collections import Counter
def anagrams(word, words):
    return [x for x in words if Counter(word) == Counter(x)]