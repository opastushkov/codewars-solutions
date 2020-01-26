def is_prime(num):
    ls = [num % x for x in range(2, num)] if num != 2 else [True]
    return all(ls) if ls else False