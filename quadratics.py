#quadratics.py

import random

def getCoeff():
    return random.randint(-6, 6)

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.a == 1:
            return f"x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"
        else:
            return f"{self.a}x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"

    def quadraticSF(self):
        if self.a == 1:
            return f"x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"
        else:
            return f"{self.a}x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"

    def quadraticVF(self):
        return "Vertex Form"

    def quadraticFF(self):
        return "Factored Form"

    def numberOfRoots(self):
        """
        Returns the number of roots that a quadratic has (0, 1, 2)
        """
        discr = (self.b)**2 - 4*self.a*self.c
        if discr > 0:
            return 2
        elif discr == 0:
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
    testB = Quadratic(1, 2, 4)
    testC = Quadratic(1, 4, 4)
    testA.report()
