def sequence_sum(b_n, e_n, s):
    return b_n + sequence_sum(b_n + s, e_n, s) if b_n <= e_n else 0