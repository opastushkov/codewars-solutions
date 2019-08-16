class Sudoku(object):


    def __init__(self, data):
        self.field = data
        
    def is_valid(self):
        size = len(self.field)
        
        for x in self.field:
            if len(x) != size:
                return False
                
        for x in range(size):
            for y in range(size):
                if type(self.field[x][y]) is not int: return False
                
        nums = [x for x in range(1, size + 1)]
        
        for x in self.field:
            if set(nums) != set(x):
                return False
                
        for x in range(size):
            temp = []
            for y in range(size):
                temp.append(self.field[y][x])
            if set(nums) != set(temp):
                return False
                
        square = []
        for x_shift in range(int(size**0.5)):
            for y_shift in range(int(size**0.5)):
                for x in range(int(size**0.5)):
                    for y in range(int(size**0.5)):
                        square.append(self.field[x + x_shift][y + y_shift])
                if set(square) != set(nums): return False
                
        return True