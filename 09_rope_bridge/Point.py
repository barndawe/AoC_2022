class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, h, v):
        self.x +=h
        self.y +=v

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y