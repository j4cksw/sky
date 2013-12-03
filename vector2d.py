#Simple vector definition

class vector2d(object):
    def __init__(self, _x=0.0, _y=00.0):
        self.x = _x
        self.y = _y
    
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
    
    @classmethod
    def from_points(cls,  p1, p2):
        return cls(p2[0] - p1[0], p2[1] - p1[1])
    
    