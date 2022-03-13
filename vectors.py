import math


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def mag(self):
        return round((self.x**2 + self.y**2 + self.z**2)**0.5, 2)

    def i(self):
        return self.x

    def j(self):
        return self.y

    def k(self):
        return self.z


def dotProduct(aVec, bVec):
    return aVec.i() * bVec.i() + aVec.j() * bVec.j() + aVec.k() * bVec.k()

def crossProduct(aVec, bVec):
    xComp = aVec.j() * bVec.k() - aVec.k() * bVec.j()
    yComp = aVec.k() * bVec.i() - aVec.i() * bVec.k()
    zComp = aVec.i() * bVec.j() - aVec.j() * bVec.i()
    cVec = Vector(xComp, yComp, zComp)
    return cVec

if __name__ == '__main__':
    a = Vector(1,2,3)
    b = Vector(2,3)
    print(b)
