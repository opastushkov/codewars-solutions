def isValidWalk(walk):
    x_c = 0
    y_c = 0
    for x in walk:
        if x == 'n': y_c += 1
        elif x == 's': y_c -= 1
        elif x == 'w': x_c -= 1
        elif x == 'e': x_c += 1
    return x_c == 0 and y_c == 0 and len(walk) == 10 