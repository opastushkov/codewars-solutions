def accum(s):
    return '-'.join([let.upper() + let.lower()*it for it, let in enumerate(s)])