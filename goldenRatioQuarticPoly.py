


def getQuartic():
    """ Returns coefOut which will be the coefficients as a list of floats.
 """
    done = False
    while not done:
        coefOut = []
        print('Enter instructions on how to enter here.')
        stringIn = input('Enter the quartic coefficients:')
        listIn = stringIn.split()
        for item in listIn:
            try:
                coefOut.append(float(item))
            except:
                break
        if len(coefOut) == 5:
            done = True
        else:
            print('Enter 5 coefficients.')
            print('Make sure to enter zero coefficients')
    return coefOut

def twoInflectionPoints(coefIn):
    a = 12 * coefIn[0]
    b = 6 * coefIn[1]
    c = 2 * coefIn[2]
    discr = b**2 - 4 * a * c 
    if discr > 0:
        print('True')
        return True
    print('False')
    return False

def inflectionPoints():
    """return two x values where the inflection points are
    """

def findY_Quartic(qIn):
    """find the y value of a quartic given the coefficients that are in qIn"""



quartic = getQuartic()
twoInflectionPoints(quartic)




