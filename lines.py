import points

class Line:

    def __init__(self, m, b):
        self.m = m
        self.b = b

    def outCoeffM(self):
        if self.m == 0:
            return ""
        elif self.m < 0:
            return f"-{abs(self.m)}x"
        else:
            return f"{self.m}x"

    def outCoeffB(self):
        if self.b == 0:
            return ""
        elif self.b < 0 and self.m == 0:
            return f"-{abs(self.b)}"
        elif self.b < 0:
            return f"- {abs(self.b)}"
        else:
            return f" + {self.b}"

    def intersect(self, other):
        x = (other.b - self.b)/(self.m - other.m)
        y = other.m * x + other.b
        return points.Point(x, y)


    def __str__(self):
        if self.m == 1:
            return f"y = x{self.outCoeffB()}"
        elif self.m == -1:
            return f"y = -x{self.outCoeffB()}"
        elif self.m == 0 and self.b > 0:
            return f"y = {self.b}"
        else:
            return f"y = {self.outCoeffM()}{self.outCoeffB()}"


#**********************************************************
if __name__ == "__main__":
    import random
    for i in range(20):
        a = random.randint(-5, 5)
        b = random.randint(-5, 5)
        aLine = Line(a, b)
        print(aLine)
        del(aLine)
