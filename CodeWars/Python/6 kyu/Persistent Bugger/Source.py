def persistence(n):
    counter = 0
    while len(str(n)) > 1:
        num = 1
        for x in str(n):
            num *= int(x)
        n = num
        counter += 1
    return counter