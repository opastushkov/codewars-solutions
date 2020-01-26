def single_digit(n):
    while len(str(n)) > 1:
        n = sum([int(x) for x in bin(n)[2:]])
    return n