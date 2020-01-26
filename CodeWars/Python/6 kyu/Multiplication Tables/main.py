import numpy as np
def multiplication_table(row,col):
    return np.array([(x//col + 1)*(x%col + 1) for x in range(row*col)]).reshape(row, col).tolist()