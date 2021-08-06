import math
class calculator():
    """A basic calculator class."""
    def __init__(self, defaultTrig = False):
        """Default for trignometry is radians. Put in 'True' for degrees. You can also choose which to use on a case-by-case."""
        self._defaultTrig = defaultTrig

    def absolute(self, number):
        return math.fabs(number)
    
    def sum(self, numbers):
        result = 0
        for i in numbers:
            result += i
        return result
    def product(self, numbers):
        result = 1
        for i in numbers:
            result *= i
        return result
    def divide(self, numer, denom):
        if denom == 0:
            raise ValueError("Cannot divide by zero.")
        else:
            return numer/denom

    def power(self, base, exp):
        return base**exp

    def logarithm(self, base, num):
        if base == 'ln':
            return math.log(num)
        else:
            return math.log10(num)

    def trig(self, function, number, useDef = True):
        #if useDef is true and defaultTrig is false, that means to use radians, and therefore will skip the radians to degrees conversion. Same if useDef is false and defaultTrig is true. Otherwise, does the conversion
        if (not useDef) ^ self._defaultTrig:
            number = number * math.pi/180

        if function == "sin":
            result = math.sin(number)
        elif function == 'cos':
            result = math.cos(number)
        elif function == 'tan':
            #the following if statement checks if the tangent would return undefined.
            if (number == (math.pi/2 or 3*math.pi/2) and not currentTrig) or (number == (90 or 270) and currentTrig):
                raise ValueError("Invalid tangent")
            else:
                result = math.tan(number)
        elif function == "csc":
            if (currentTrig and number == (180 or 0)) or (not currentTrig and number == (math.pi or 0)):
                raise ValueError("Invalid cosecant")
            else:
                result = 1/math.sin(number)
        elif function == "sec":
            if (currentTrig and number == (90 or 270)) or (not currentTrig and number == (math.pi/2 or 3*math.pi/2)):
                raise ValueError("Invalid secant")
            else:
                result = 1/math.cos(number)
        elif function == "cot":
            if (number == (math.pi or 0) and not currentTrig) or (number == (180 or 0) and currentTrig):
                raise ValueError("Invalid cotangent")
            else:
                result = 1/math.tan(number)

        return result
    def invTrig(self, function, number, useDef = True):
        #if useDef is true and defaultTrig is false, that means to use radians, and therefore will skip the radians to degrees conversion. Same if useDef is false and defaultTrig is true. Otherwise, does the conversion
        if (not useDef) ^ self._defaultTrig:
            currentTrig = True #means degrees
        else:
            currentTrig = False #means radians

        if function == "arcsin":
            result = math.asin(number)
        elif function == 'arccos':
            result = math.acos(number)
        elif function == 'arctan':
            result = math.atan(number)
        if currentTrig:
            result = result * 180/math.pi
        return result
    def setDefTrig(self, val):
        self._defaultTrig = val
    def getDefTrig(self):
        return self._defaultTrig