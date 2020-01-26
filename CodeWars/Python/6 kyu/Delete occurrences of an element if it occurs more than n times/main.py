def delete_nth(order,max_e):
    ls = []
    for x in order:
        if ls.count(x) < max_e:
            ls.append(x)
    return ls