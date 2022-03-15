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

class VPlane:
    def __init__(self, *args):
        if len(args) == 3:
            print("Vector Form")
            self.pVec = args[0]
            self.d1Vec = args[1]
            self.d2Vec = args[2]
            self.form = "VF"
        elif len(args) == 4:
            print("Standard Form")
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]
            self.form = "SF"
        else:
            print("potato")


    def __str__(self):
        if self.form == "VF":
            return f"r = {self.pVec} + s{self.d1Vec} +  t{self.d2Vec}"
        elif self.form == "SF":
            return f"{self.a}x + {self.b}y + {self.c}z + {self.d} = 0"

    def normal(self):
        return self.d1Vec.cross(self.d2Vec)

if __name__ == '__main__':
    a = VPlane(1,2,3,4)
    print(a, a.form)
