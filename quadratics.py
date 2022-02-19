#quadratics.py

import random

def getCoeff():
    return random.randint(-6, 6)

class Quadratic:
    def __init__(self):
        self.a = getCoeff()
        self.b = getCoeff()
        self.c = getCoeff()

    def coeffB(self):
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

    def coeffC(self):
        if self.c == 0:
            return ""
        elif self.c < 0:
            return f" - {abs(self.c)}"
        else:
            return f" + {self.c}"

    def __str__(self):
        if self.a == 1:
            return f"x\N{SUPERSCRIPT TWO}{self.coeffB()}{self.coeffC()}"
        elif self.a == -1:
            return f"-x\N{SUPERSCRIPT TWO}{self.coeffB()}{self.coeffC()}"
        else:
            return f"{self.a}x\N{SUPERSCRIPT TWO} + {self.coeffB()}x + {self.coeffC()}"



class SimpleF(Quadratic):
    def __init__(self):
        self.a = 1
        self.b = getCoeff()
        self.c = getCoeff()


    for i in range(10):
        a = SimpleF()
        print(a)
