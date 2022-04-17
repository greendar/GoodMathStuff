from vectors import *

def magAdd(u, v, angle):
    sum = u.mag()**2 + v.mag()**2
    sum += 2 * u.mag() * v.mag() * math.cos(math.radians(angle))
    return int(round(sum, 0))

A = Vector(4, -2, 5)
B = Vector(8, -4, 10)
C = Vector(1, 3, -2)
D = A + C
E = A - C
F = Vector(2, 4, 0)
G = Vector(B.x, B.y)
R0 = Vector(2, -3)
iHat = Vector(1, 0)
M = Vector(-5, 1, 3)

report = f"""Page 1**************************************************
A = {A}
B = {B}  {A.checkParallel(B)}
C = {C}
A+C = {A+C}
A-C = {A-C}
F = {F} {A.checkPerpendicular(F)}
Page 2***********************************************************
magA = {A.mag()}    unitA {A.scalarMult(1/A.mag())}
AdotC = {A.dot(C)}   AcrossC = {A.cross(C)}
AangleC = {int(round(A.angle(C), 0))} deg
|A + C| = {magAdd(A, C, int(round(A.angle(C), 0)))}
Proof:   {E.cross(D)} = {A.scalarMult(2).cross(C)}
Page 3***********************************************************
G = {G}
R = {R0} + t{G}
Parametric Eqns    x = {R0.x} + {G.x}t    y = {R0.y} + {G.y}t
Symmetric Eqns     (x - {R0.x})/{G.x} = (y - {R0.y})/{G.y}
Standard Form    {G.y}x - {G.x}y + {-(G.y*2 + G.x * (-3))} = 0
Point (5, 7)    {(5-R0.x)/G.x}, {(7-R0.y)/G.y} {(5-R0.x)/G.x == (7-R0.y)/G.y}
Angle With xAxis:  {int(round(G.angle(iHat), 0))}
Page 4***********************************************************
R = {C} + t{A}
Parametric  x = {C.x} + {A.x}t, y = {C.y} + {A.y}t, z = {C.z} + {A.z}t
Symmetric   (x - {C.x})/{A.x} = (y - {C.y})/{A.y} = (z - {C.z})/{A.z}
Standard Form: CANNOT DO FOR 3D LINE
t = 2
t = 0   {C}
t = -3
Intersection Angle  {int(round(A.angle(M), 0))}
"""
print(report)
