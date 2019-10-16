class Vector():

    def __str__(self):
        return "({})".format(",".join(map(str, self.coor)))
    
    def __init__(self, ls):
        self.coor = ls

    def add(self, other):
        return Vector([a + b for a,b in zip(self.coor, other.coor)])
        
    def equals(self, other):
        return all(a == b for a, b in zip(self.coor, other.coor))

    def subtract(self, other):
        return Vector([a - b for a,b in zip(self.coor, other.coor)])
        
    def dot(self, other):
        return sum([a * b for a,b in zip(self.coor, other.coor)])
        
    def norm(self):
        return sum(x**2 for x in self.coor) ** 0.5

        