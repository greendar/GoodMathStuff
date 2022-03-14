class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distFromOrig(self):
        return ((self.x**2 + self.y**2)**0.5)

    def __str__(self):
        return f"({self.x}, {self.y})"
