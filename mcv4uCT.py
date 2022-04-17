from vectors import *

def magAdd(u, v, angle):
    sum = u.mag()**2 + v.mag()**2
    sum += 2 * u.mag() * v.mag() * math.cos(math.radians(angle))
    return int(round(sum, 0))

A = Vector(1, 2, -3)
B = Vector(2, 4, -6)
C = Vector(-3, 1, 2)
D = A + C
E = A - C
F = Vector(-2, 1, 0)
G = Vector(B.x, B.y)
R0 = Vector(2, -3)

report = f"""Page 1
A = {A}
B = {B}  {A.checkParallel(B)}
C = {C}
A+C = {A+C}
A-C = {A-C}
F = {F} {A.checkPerpendicular(F)}

Page 2
magA = {A.mag()}    unitA {A.scalarMult(1/A.mag())}
AdotC = {A.dot(C)}   AcrossC = {A.cross(C)}
AangleC = {int(round(A.angle(C), 0))} deg
|A + C| = {magAdd(A, C, int(round(A.angle(C), 0)))}
Proof:   {E.cross(D)} = {A.scalarMult(2).cross(C)}

Page 3
G = {G}
R = {R0} + t{G}
Parametric Equations
    x = {R0.x} + {G.x}t
    y = {R0.y} + {G.y}t
Symmetric Equations
    (x - {R0.x})/{G.x} = (y - {R0.y})/{G.y}
Standard Form
    {G.y}x - {G.x}y + {-(G.y*2 + G.x * (-3))} = 0
"""
print(report)
