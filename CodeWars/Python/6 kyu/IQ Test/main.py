def iq_test(numbers):
    ls = [int(x) % 2 == 0 for x in numbers.split()]
    return ls.index(True) + 1 if sum(ls) == 1 else ls.index(False) + 1