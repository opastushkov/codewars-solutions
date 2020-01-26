def in_array(a1, a2):
    ls = []
    for x in a1:
        for y in a2:
            if x in y: ls.append(x)
    return sorted(list(set(ls)))