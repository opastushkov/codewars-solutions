def duplicate_encode(word):
    return ''.join(['(' if word.upper().count(x) == 1 else ')' for x in word.upper()])