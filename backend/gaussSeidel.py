# Gauss Seidel algorithm using golden seaction search as optimization method in specific direction
from sympy import *
import math
#from math import *


# p0 is a whole starting point, n is a number of variables in function
from backend.goldenSectionSearch import goldenSectionSearch

XL = -5     # lower bound for golden section search
XU = 5      # upper bound for golden section search
pointList = []  # first element is the initial guess, the rest is coming from algorithm iterations
twoPointDistArr = []
twoPointDist = 1000
calculationLogsString = ""


# Function adds value of given point to the POINT vector
def changePoint(point, argNumber, argValue):
    newPoint = point.copy()
    newPoint[argNumber] = argValue
    return newPoint

# ARGs:
# function - given function by the user for the optimization task
# precision - ??
# L - max number of iterations
# p0 - starting point chosen by the user
# intervalLength
def gaussSeidel(function, givenExpression, precison, L, p0, intervalLength, accuracyX, accuracyFX, calculationLogsString):
    i = 0
    it = 0
    point = p0              # first point is our initial guess
    funcValDiff = 10000
    twoPointDist = 10000
    pointList.append(p0)    # adding initial point (guess) to list of all points
    n = len(point)          # number of entered function variables

    #while (i < L and funcValDiff > accuracyFX and twoPointDist > accuracyX):
    while (i < L and funcValDiff > accuracyFX and twoPointDist > accuracyX):
        for pos in range(n):
            xl = point[pos] - intervalLength
            xu = point[pos] + intervalLength

            f = lambda x: function(givenExpression, changePoint(point, pos, x))
            value = goldenSectionSearch(f, xl, xu, accuracyX/10)      # value is xopt
            point = changePoint(point, pos, value)

        pointList.append(point)
        i += 1
        it += 1

        # computing one of the stop criterion - difference between 2 function values for specific points
        if len(pointList) >= 2:
            funcValDiff = abs(function(givenExpression, pointList[it]) - function(givenExpression, pointList[it - 1]))

        # computing one of the stop criterion - distance diff between 2 points
        twoPointDistArr.clear()
        if len(pointList) >= 2:
            for z in range(n):
                diff = abs(pointList[it][z] - pointList[it-1][z])
                #print("Diff: ")
                #print(diff)
                twoPointDistArr.append(diff)

            dist = 0
            for elem in range(len(twoPointDistArr)):
                if(twoPointDistArr[elem] > dist):
                    dist = twoPointDistArr[elem]
            twoPointDist = dist
        print()
        print("Numer iter: ", i)
        calculationLogsString = calculationLogsString + str("Num iter: " + str(i))
        print("Aktualny punkt: ", pointList[i])
        calculationLogsString = calculationLogsString + str(", Punkt: ")
        for j in range(n):
            p = pointList[i][j]
            p=float(f'{p:.4f}')
            print("P to: " + str(p))
            calculationLogsString = calculationLogsString + str(p) + ", "
        #calculationLogsString = calculationLogsString + str(", Punkt: " + str(pointList[i]))
        print("Wartosc funkcji: ")
        print(function(givenExpression, pointList[it]))
        #calculationLogsString = calculationLogsString + str(" F(P_i): " + str(function(givenExpression, pointList[it])))
        #strFuncVal = str(round(function(givenExpression, pointList[it]), 4))
        strFuncVal = str(float(f'{function(givenExpression, pointList[it]):.4f}'))
        calculationLogsString = calculationLogsString + str(" F(P_i): " + strFuncVal)

        calculationLogsString = calculationLogsString + "\n"

        print("Wartości kryt stopu")
        print("Różnica wart funkcji: ", funcValDiff, "Dystans pomiędzy dwoma punktami: ", twoPointDist)


    print("STR: ")
    print(calculationLogsString)
    # printing
    print("Parametry do stopu: ")
    print("ilosc zrobionych iteracji: ")
    print(i)
    print("Roznica w wartosci funkcji: ")
    print(funcValDiff)
    print("Najwieksza roznica w odleglosci miedzy dwoma pkt: ")
    print(twoPointDist)
    if(funcValDiff < accuracyFX):
        calculationLogsString += "Kryt stopu: funcValDiff " + str(float(f'{funcValDiff:.6f}'))
        print("ZATRZYMANE PRZEZ: funcValDiff")
    if(twoPointDist < accuracyX):
        print("ZATRZYMANE PRZEZ: twoPointDist")
        calculationLogsString += " Kryt stopu: twoPointDist " + str(float(f'{twoPointDist:.6f}'))
    if (i >= L):
        print("ZATRZYMANE PRZEZ: liczbe iteracji")
        calculationLogsString += "Kryt stopu: ilosc iteracji: " + str(i)
    print("Lista punktow")
    print(pointList)
    return pointList, calculationLogsString
