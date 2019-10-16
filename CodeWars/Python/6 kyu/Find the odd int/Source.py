def find_it(seq):
    return [x for x in set(seq) if seq.count(x) % 2 == 1][0]
