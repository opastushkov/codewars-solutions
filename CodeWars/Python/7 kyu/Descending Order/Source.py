def Descending_Order(num):
    return int(''.join([str(x) for x in sorted([int(x) for x in str(num)], reverse=True)]))