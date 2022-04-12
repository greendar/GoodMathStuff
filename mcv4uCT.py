from vectors import *

A = Vector(3, 5, -2)
B = Vector(6, 10, -4)
C = Vector(4, 1, -3)
F = Vector(-3, -7, -22)

report = f"""Page 1
A = {A}
B = {B}  {A.checkParallel(B)}
C = {C}
A+C = {A+C}
A-C = {A-C}
F = {F} {A.checkPerpendicular(F)}

Page 2
magA = {A.mag()}

AdotC = {A.dot(C)}   AcrossC = {A.cross(C)}
AangleC = {int(round(A.angle(C), 0))} deg

"""
print(report)
