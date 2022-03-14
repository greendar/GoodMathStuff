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

    def dot(self, other):
        return self.i() * other.i() + self.j() * other.j() + self.k() * other.k()

    def cross(self, other):
        xComp = self.j() * other.k() - self.k() * other.j()
        yComp = self.k() * other.i() - self.i() * other.k()
        zComp = self.i() * other.j() - self.j() * other.i()
        cVec = Vector(xComp, yComp, zComp)
        return cVec

    def angle(self, other):
        return math.degrees(math.acos(self.dot(other)/(self.mag()*other.mag())))

class vLine:
    def __init__(self, pVec, dVec):
        self.pVec = pVec
        self.dVec = dVec

    def __str__(self):
        return f"r = {self.pVec} + t{self.dVec}"

class vPlane:
    def __init__(self, pVec, d1Vec, d2Vec):
        self.pVec = pVec
        self.d1Vec = d1Vec
        self.d2Vec = d2Vec

    def __str__(self):
        return f"r = {self.pVec} + s{self.d1Vec} +  t{self.d2Vec}"

    def normal(self):
        return self.d1Vec.cross(self.d2Vec)

if __name__ == '__main__':
    a = Vector(1,2, 4)
    b = Vector(4,1,3)
    c = Vector(3,5,6)
    plane = vPlane(a, b, c)
    print(plane)
    print(plane.normal())
