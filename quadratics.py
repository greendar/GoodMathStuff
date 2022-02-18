#quadratics.py

import random

def getCoeff():
    return random.randint(-6, 6)

class Quadratic:
    def __init__(self):
        self.a = getCoeff()
        self.b = getCoeff()
        self.c = getCoeff()

    def __str__(self):
        if self.a == 1:
            return f"x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"
        else:
            return f"{self.a}x\N{SUPERSCRIPT TWO} + {self.b}x + {self.c}"



class SimpleF(Quadratic):
    def __init__(self):
        self.a = 1
        self.b = getCoeff()
        self.c = getCoeff()


if __name__ == "__main__":
    for i in range(100):
        a = SimpleF()
        print(a)
