"""
program to make up questions for difference of squares problems
of simple and complex type
"""

import random as r

def getSign():
    getNum = r.randint(1,2)
    if getNum == 1:
        return -1
    elif getNum == 2:
        return 1

def getCoeff(absMax):
    notDone = True
    while notDone:
        num = r.randint(1, absMax)
        if num != 0:
            notDone = False
    return num

def getEvenCoeff():
    notDone = True
    while notDone:
        num = r.randint(1, 6)
        if num != 0:
            notDone = False
    return 2 * num


for i in range(20):
    print(getSign()*getEvenCoeff(), getSign() * getCoeff(23))
    
