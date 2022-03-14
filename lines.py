import points

class Line:

    def __init__(self, m, b):
        self.m = m
        self.b = b

    def outCoeffM(self):
        if self.m == 0:
            return ""
        elif self.m == 1:
            return f" + x"
        elif self.m == -1:
            return f" - x"
        elif self.m < 0:
            return f" - {abs(self.m)}x"
        else:
            return f" + {self.m}x"

    def outCoeffB(self):
        if self.b == 0:
            return ""
        elif self.b < 0:
            return f" - {abs(self.b)}"
        else:
            return f" + {self.b}"

    def intersect(self, other):
        x = (other.b - self.b)/(self.m - other.m)
        y = other.m * x + other.b
        return points.Point(x, y)


    def __str__(self):
        if self.m == 1:
            return f"x{self.outCoeffB()}"
        elif self.m == -1:
            return f"-x{self.outCoeffB()}"
        else:
            return f"{self.outCoeffM()}x{self.outCoeffB()}"


#**********************************************************
if __name__ == "__main__":
    testA = Line(11, 5)
    testB = Line(0, -2)
    testC = Line(-4, 4)
    print("A", testA.intersect(testC))
