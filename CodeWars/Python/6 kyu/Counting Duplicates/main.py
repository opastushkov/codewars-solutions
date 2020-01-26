def duplicate_count(text):
    return sum([1 for x in set(text) if text.lower().count(x) > 1])
     