def isSolved(board):

    for x in board:
        if set(x) == set([2]):
            return 2
        elif set(x) == set([1]):
            return 1
            
    for x in range(len(board)):
        ls = []
        for y in range(len(board)):
            ls.append(board[y][x])
        if set(ls) == set([2]):
            return 2
        elif set(ls) == set([1]):
            return 1
            
    ls = []
    for x in range(len(board)):
        ls.append(board[x][x])
    if set(ls) == set([2]):
        return 2
    elif set(ls) == set([1]):
        return 1
    
    del ls
    ls = []
    for x in range(len(board)):
        ls.append(board[x][len(board) - x - 1])
    if set(ls) == set([2]):
        return 2
    elif set(ls) == set([1]):
        return 1
        
    return -1 if any([0 in x for x in board]) else 0
        