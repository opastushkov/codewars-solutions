from itertools import permutations as p
def permutations(s):
    return set([''.join(x) for x in p(s)])