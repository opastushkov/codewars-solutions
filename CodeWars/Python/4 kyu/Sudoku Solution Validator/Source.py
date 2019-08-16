def validSolution(board):
    num = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in board:
        if set(i) != num: return False
    for x in range(9):
        line = []
        for y in range(9):
            line.append(board[y][x])
        if set(line) != num: return False
    for step_x in range(3):
        for step_y in range(3):
            square = []
            for x in range(3):
                for y in range(3):
                    square.append(board[x + step_x * 3][y + step_y * 3])
            if set(square) != num: return False
    return True
            