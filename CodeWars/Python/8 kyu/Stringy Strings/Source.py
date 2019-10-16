def stringy(size):
    print(size)
    return "".join(['1' if x % 2 == 0 else '0' for x in range(size)])