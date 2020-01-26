def find_outlier(integers):
    ls = [x % 2 == 0 for x in integers]
    return integers[ls.index(True)] if sum(ls) == 1 else integers[ls.index(False)]