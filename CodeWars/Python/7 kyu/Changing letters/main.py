def swap(st):
    return "".join(x.upper() if x in ['a', 'o', 'u', 'i', 'e'] else x for x in st)