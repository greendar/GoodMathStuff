"""
Creates the function doMath that will do different things depending on how many arguments are passed
"""

def doMath(*args):
    a = args
    if len(args) == 2:
        return args[0]/args[1]
    elif len(args) == 1:
        return args[0]
    elif len(args) == 3:
        return args[0]*args[1]*args[2]
    elif len(args) > 3:
        sum = 0
        for num in args:
            sum += num
        return sum
    else:
        return "potato"


print(doMath(1,2,3,4,5,6))
print(doMath(1,2,3))
print(doMath(1,2))
print(doMath(1))
print(doMath())
