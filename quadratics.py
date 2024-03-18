#quadratics.py
from mathErrors import NonQuadraticError

import random

def getCoeff():
    return random.randint(-6, 6)

class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a == 0:
            raise NonQuadraticError(self.a)

    def outCoeffB(self):
        """Used for printing B."""
        if self.b == 0:
            return ""
        elif self.b == 1:
            return f" + x"
        elif self.b == -1:
            return f" - x"
        elif self.b < 0:
            return f" - {abs(self.b)}x"
        else:
            return f" + {self.b}x"

    def outCoeffC(self):
        """Used for printing C."""
        if self.c == 0:
            return ""
        elif self.c < 0:
            return f" - {abs(self.c)}"
        else:
            return f" + {self.c}"

    def discr(self):
        return (self.b)**2 - 4*self.a*self.c

    def __str__(self):
        if self.a == 1:
            return f"x\N{SUPERSCRIPT TWO}{self.outCoeffB()}{self.outCoeffC()}"
        elif self.a == -1:
            return f"-x\N{SUPERSCRIPT TWO}{self.outCoeffB()}{self.outCoeffC()}"
        else:
            return f"{self.a}x\N{SUPERSCRIPT TWO} + {self.outCoeffB()}x + {self.outCoeffC()}"

    def quadraticSF(self):
        if self.a == 1:
            return f"x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"
        else:
            return f"{self.a}x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"

    def quadraticVF(self):
        self.h = self.b/(2*self.a)
        self.k = self.c - (self.b**2)/(4*self.a)
        if self.a == 1:
            return f"(x+{self.h})\N{SUPERSCRIPT TWO} + {self.k}"
        else:
            return f"{self.a}(x+{self.h})\N{SUPERSCRIPT TWO} + {self.k}"

    def quadraticFF(self):
        return "Factored Form"

    def numberOfRoots(self):
        """
        Returns the number of roots that a quadratic has (0, 1, 2)
        """
        if self.discr() > 0:
            return 2
        elif self.discr() == 0:
            return 1
        else:
            return 0

    def report(self):
        """
        Prints information to the screen.
        Print:
            Quadratic
            Vertex
            Roots
            y-Intercept
        """
        print("Quadratic Report\n")
        print(f"Standard Form: y = {self.quadraticSF()}")
        print(f"  Vertex Form: y = {self.quadraticVF()}")
        print(f"Factored Form: y = {self.quadraticFF()}")
        print(f"\n  y-Intercept: (0, {self.c})")
        print(f"   # of Roots: {self.numberOfRoots()}")
        print(f"       Vertex: Vertex")


class SimpleF(Quadratic):
    def __init__(self):
        self.a = 1
        self.b = getCoeff()
        self.c = getCoeff()



#*****************************************************************
if __name__ == "__main__":
    testA = Quadratic(1, 5, 6)
    testB = Quadratic(1, -2, 4)
    testC = Quadratic(1, 4, -4)
    print("A", testA)
    print("B", testB)
    print("C", testC)
    testA.report()
