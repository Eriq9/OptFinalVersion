# Main project file
#from math import *
import math
from backend.gaussSeidel import gaussSeidel
from backend.goldenSectionSearch import goldenSectionSearch
INTERVAL_LENGTH = 10

class OptimizationAlgorithm:
    def __init__(self, expression, L, initialPoint, intervalLength, accuracyX, accuracyFX):
        self.givenExpression = expression
        self.L = L
        self.p_example = initialPoint
        self.intervalLength = intervalLength
        self.accuracyX = accuracyX
        self.accuracyFX = accuracyFX
        self.calculationLogsString = ""

    # function that return mathematical evaluation of given string
    def functionExample(expression, point):

        X = point[0]
        Y = point[1]
        if(len(point) >= 3):
            Z = point[2]
        if(len(point) >= 4):
            V = point[3]
        if(len(point) >= 5):
            W = point[4]
        return eval(expression)      # funkcja testowa

    def runAlgorithm(self):
        #p_example = [4.5, -1]
        precision = 0.01
        #L = 5

        # ARGs:
        # functionExample - function that returns evaluated expression from string input
        # givenExpression - mathematical expression entered by user, string
        # precision - stop criteria
        # L - max number of iterations
        # p_example - starting point chosen by the user
        # intervalLength -

        #pointList = gaussSeidel(OptimizationAlgorithm.functionExample, self.givenExpression, precision, int(self.L), self.p_example, float(self.intervalLength), float(self.accuracyX), float(self.accuracyFX), self.calculationLogsString)
        result = gaussSeidel(OptimizationAlgorithm.functionExample, self.givenExpression, precision, int(self.L), self.p_example, float(self.intervalLength), float(self.accuracyX), float(self.accuracyFX), self.calculationLogsString)
        pointList = result[0]
        calculationLogsString = result[1]

        return pointList, calculationLogsString


    # ZMIENIC WYPISYWANIE W GOLDEN SECTION, NIECH WYPISUJE W GAUSIE PUNKTY w zaleznosci do iteracji
    # dopisać pozostałe warunki stopu
    # zastanowic sie nad przedziałem ??? ( da sie go automatycznie przesuwać)? spytac
    # DLA WIEKSZEJ ILOSCI WYMIARÓW ?? spytac // no tak ma byc
    # poczatek przedzialu to wartosc punktu poczatkowego, a koniec przedzialu podawany jako parametr
    # wykres z poziomicami


#Liniowe: Graficzna i dwufazowa metoda Simplex