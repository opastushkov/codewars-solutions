def move_zeros(array):
    counter = 0
    res = []
    for x in array:
        if type(x) is bool or x != 0: res.append(x) 
        else: counter += 1
    for x in range(counter):
        res.append(0)
    return res