def to_underscore(s):

    word = s[0].lower() if type(s) is str else ''
    ls = []
    
    if not word: return str(s)
    
    for x in range(1, len(s)):
        if not s[x].isupper():
            word += s[x]
        if s[x].isupper() or x == len(s) - 1:
            ls.append(word)
            word = ''
            word += s[x].lower()
    
    return '_'.join(ls)