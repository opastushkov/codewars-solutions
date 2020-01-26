def solution(args):
    res = ''
    it = 0
    temp = 0
    while it < len(args):
        start = it
        if it < len(args) - 1:
            temp = args[it + 1]
        while temp - args[it] == 1:
            it += 1
            if it < len(args) - 1:
                temp = args[it + 1]

        if start == it:
            res += str(args[it]) + ','
        elif it - start == 1:
            it -= 1
            res += str(args[it]) + ','
        else:
            res += str(args[start]) + '-' + str(args[it]) + ','

        it += 1

    return res[:-1]