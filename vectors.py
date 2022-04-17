import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        if self.z == 0:
            return f"[{self.x}, {self.y}]"
        else:
            return f"[{self.x}, {self.y}, {self.z}]"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def scalarMult(self, scalar):
        return Vector(round(self.x*scalar, 3), round(self.y*scalar, 3), round(self.z*scalar, 3))
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
        """
        Returns the angle in degrees between two vectors
        """
        return math.degrees(math.acos(self.dot(other)/(self.mag()*other.mag())))

    def checkParallel(self, other):
        """
        Checks if two vectors are scalar multiples of each other and returns True or False
        """
        if self.x/other.x == self.y/other.y and self.x/other.x == self.z/other.z:
            return True
        else:
            return False

    def checkPerpendicular(self, other):
        if self.dot(other) == 0:
            return True
        else:
            return False


class vLine:
    def __init__(self, pVec, dVec):
        self.pVec = pVec
        self.dVec = dVec

    def __str__(self):
        return f"r = {self.pVec} + t{self.dVec}"

class VPlane:
    def __init__(self, *args):
        if len(args) == 3:
            self.pVec = args[0]
            self.d1Vec = args[1]
            self.d2Vec = args[2]
            self.form = "VF"
        elif len(args) == 4:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]
            self.form = "SF"
        else:
            print("Unrecognized Form")################

    def normal(self):
        return self.d1Vec.cross(self.d2Vec)

    def outCoeffA(self):
        if self.a == 0:
            return ""
        elif self.a == 1:
            return f"x"
        elif self.a == -1:
            return f"-x"
        elif self.a < 0:
            return f"-{abs(self.a)}x"
        else:
            return f"{self.a}x"

    def outCoeffB(self):
        if self.b == 0:
            return ""
        elif self.b == 1:
            return f" + y"
        elif self.b == -1:
            return f" - y"
        elif self.b < 0:
            return f" - {abs(self.b)}y"
        else:
            return f" + {self.b}y"

    def outCoeffC(self):
        if self.c == 0:
            return ""
        elif self.c == 1:
            return f" + z"
        elif self.c == -1:
            return f" - z"
        elif self.c < 0:
            return f" - {abs(self.c)}z"
        else:
            return f" + {self.c}z"

    def outCoeffD(self):
        if self.d == 0:
            return ""
        elif self.d < 0:
            return f" - {abs(self.d)}"
        else:
            return f" + {self.d}"


    def threePoints(self):
        """
        This method will use the intersection of two sets of factors to find a solution
        for two values of x/y/z. It is assumed that the other is equal to zero.
        Coefficients are:
        self.a = x Var
        self.b = y Var
        self.c = z Var
        self.d = constant

        CURRENT ERROR
        2x + 2y - z - 2 = 0   ==>   [1, 0, 0] Good
                                    [2, 1, 0] Bad, should be [2, -1, 0]
                                    [0, 1, 0]

        """
        aList = []
        bList = []

        for i in range(-5, 5):
            aList.append(self.a*i+self.d)
            bList.append(self.b*i)

        aOut = set(aList)
        bOut = set(bList)
        intersectOut = aOut.intersection(bOut)
# what to do if intersectOut is an empty set
        outList = []
        for item in intersectOut:
            tempList = []
            tempList.append(int((item-self.d)/self.a))
            tempList.append(int(item/self.b))
            tempList.append(int(0))
            outList.append(tempList)
            if len(outList) == 2:
                break

        bList = []
        cList = []

        for i in range(-5, 5):
            bList.append(self.b*i+self.d)
            cList.append(self.c*i)

        bOut = set(bList)
        cOut = set(cList)
        intersectOut = bOut.intersection(cOut)
# what to do if intersectOut is an empty set
        for item in intersectOut:
            tempList = []
            tempList.append(int(0))
            tempList.append(int((item-self.d)/self.b))
            tempList.append(int(item/self.c))
            outList.append(tempList)
            if len(outList) == 3:
                break

        return outList


    def __str__(self):
        if self.form == "VF":
            return f"r = {self.pVec} + s{self.d1Vec} +  t{self.d2Vec}"
        elif self.form == "SF":
            return f"{self.outCoeffA()}{self.outCoeffB()}{self.outCoeffC()}{self.outCoeffD()} = 0"


if __name__ == '__main__':
    import random

    def nonZero():
        while True:
            num = random.randint(-5, 5)
            if num != 0:
                return num

    for i in range(10):
        a = nonZero()
        b = nonZero()
        c = nonZero()
        d = nonZero()
        aPlane = VPlane(a, b, c, d)
        print(aPlane, aPlane.threePoints())
        del(aPlane)
