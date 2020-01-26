def unique_in_order(it):
    if not it: return []
    ls = [it[x] for x in range(len(it) - 1) if it[x+1] != it[x]]
    if not ls or ls[-1] != it[-1]: ls.append(it[-1])
    return ls