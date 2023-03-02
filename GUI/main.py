import tkinter
from cgitb import reset
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from backend import main
import math
from tkinter.scrolledtext import ScrolledText

#General
from tkinter import messagebox

from backend.main import OptimizationAlgorithm

root = Tk()
root.title('Gauss - Seidl Algorithm')
root.geometry("1200x600")
root.resizable(True,True)

#frame_radioButtons = tkinter.Frame(root)
#frame_radioButtons.place(x=300, y=300)

#Labels

Label(root, text="Gauss - Seidl Algorithm",font=("Helvetica", 18)).place(x=350, y=25)           #Title label
Label(root, text="Results:",font=("Helvetica", 14)).place(x=700, y=90)                          #Results label
Label(root, text="Enter your function:",font=("Helvetica", 10)).place(x=20, y=100)              #Function label
Label(root, text="Enter end of range:",font=("Helvetica", 10)).place(x=20, y=150)               #Range label, w zĹ‚otym podziale
Label(root, text="Enter your start point:",font=("Helvetica", 10)).place(x=20, y=200)           #Start point label
Label(root, text="Enter number of iterations:",font=("Helvetica", 10)).place(x=20, y=250)       #Number ob iterations label
Label(root, text="Function value stop:",font=("Helvetica", 10)).place(x=20, y=300)              #Function value stop
Label(root, text="Points difference stop:",font=("Helvetica", 10)).place(x=20, y=350)           #Point difference stop


Label(root, text="Choose predefined functions:",font=("Helvetica", 10)).place(x=20, y=400)      #Predefined functions label
Label(root, text="Selected options:",font=("Helvetica", 10)).place(x=20, y=450)      #Selected options label

Label(root, text="Value:",font=("Helvetica", 10)).place(x=600, y=150)      #Minimum
Label(root, text="Minimum:",font=("Helvetica", 10)).place(x=600, y=200)      #Value of functions
Label(root, text="Steps:",font=("Helvetica", 10)).place(x=600, y=250)      #Value of functions
#(root, text="Stop criterium:",font=("Helvetica", 10)).place(x=600, y=250)         #Stop criterium

#Function field

equation_Box = Entry(root, width=50)
equation_Box.place(x=180,y=101)

#Range field

range_Box = Entry(root, width=50)
range_Box.place(x=180,y=151)

#Start point field

startPoint_Box = Entry(root, width=50)
startPoint_Box.place(x=180,y=201)

#Number of iterations field

iterations_Box = Entry(root, width=50)
iterations_Box.place(x=180,y=251)

#Stop1 field, Function Value

stop1_Box = Entry(root, width=50)
stop1_Box.place(x=180,y=301)

#Stop2 field, Points Difference

stop2_Box = Entry(root, width=50)
stop2_Box.place(x=180,y=351)


#Drop down box

def display_selected(choice):

    global choiceVar
    choiceVar = variable.get()
    #print(choiceVar)

options = ['2*X^2 - 1.05*X^4 + (1/6)*X^6 + X*Y + Y^2',
           '(X-4)^2 + (X - Y^2)^2',
           '4*X^2 - 2.1*X^4 + (1/3)*X^6 + X*Y - 4*Y^2 + 4*Y^4',
           '-1.5 * x + 2.5*y + 1 + math.sin(x+y) + (x-y)**2']

variable = StringVar()
variable.set(options[0])

# creating widget
dropdown = OptionMenu(
    root,
    variable,
    *options,
    command=display_selected
)

dropdown.place(x=225, y=395)

#Accept Button

def Accept():

    global chosen

    if equation_Box.get() == "":
        chosen = "Your options are - Equation: " + variable.get() + ", Range: " + range_Box.get()  + ", Start point: " + startPoint_Box.get() + ", Number of iterations: " + iterations_Box.get() + ", Stop1: " + stop1_Box.get() + ", Stop2: " + stop2_Box.get()
    else:
        chosen = "Your options are - Equation: " + equation_Box.get() + ", Range: " + range_Box.get() + ", Start point: " + startPoint_Box.get() + ", Number of iterations: " + iterations_Box.get() + ", Stop1: " + stop1_Box.get() + ", Stop2: " + stop2_Box.get()

    global myLabel
    myLabel = Label(root, text=chosen)
    myLabel.place(x=125,y=450)

def clear():
    chosen = "                                                                                                                                                                                        " \
             "                                                                                                                                       "

    optPlace = "                                                                                                                                 "
    optValue = "                                                                                                                                 "

    myLabel = Label(root, text=chosen)
    myLabel.place(x=125, y=450)

    FunctionValueLabel = Label(root, text=optValue)
    FunctionValueLabel.place(x=700, y=150)

    MinimumLabel = Label(root, text=optPlace)
    MinimumLabel.place(x=700, y=200)


    equation_Box.delete(0, 'end')
    range_Box.delete(0, 'end')
    startPoint_Box.delete(0, 'end')
    iterations_Box.delete(0,'end')
    stop1_Box.delete(0, 'end')
    stop2_Box.delete(0, 'end')




def play():
    chosen = "                                                                                                                                                                                        " \
             "                                                                                                                                       "
    myLabel = Label(root, text=chosen)
    myLabel.place(x=125, y=450)
    Accept()

def DownloadParameters():

    global FunctionVar
    global RangeVar
    global StartPointVar
    global IterationsVar
    global FunctionVarFloat
    global StopFunctionValue
    global StopPointsDifference

    global givenExpression
    global initialPoint
    global L
    global intervalLength
    global accX
    global accFX
    #Sprawdzenie czy podana jest funkcja z boxa czy z rozwijanego menu

    FunctionVarBox = equation_Box.get()
    FunctionVarBox = FunctionVarBox.replace("^","**")
    FunctionDropDownMenu = variable.get()
    FunctionDropDownMenu = FunctionDropDownMenu.replace("^","**")
    FunctionDropDownMenu = FunctionDropDownMenu.replace("x","X")
    FunctionDropDownMenu = FunctionDropDownMenu.replace("y","Y")
    FunctionDropDownMenu = FunctionDropDownMenu.replace("z","Z")
    FunctionDropDownMenu = FunctionDropDownMenu.replace("v","V")
    FunctionDropDownMenu = FunctionDropDownMenu.replace("w","W")


    if FunctionVarBox == "":
        FunctionVar = FunctionDropDownMenu
    else:
        FunctionVar = FunctionVarBox

    FunctionVarFloat = FunctionVar.strip("\'")
    givenExpression = FunctionVar

    RangeVar = range_Box.get()
    StartPointVar = startPoint_Box.get()
    IterationsVar = iterations_Box.get()
    StopFunctionValue = stop1_Box.get()                                              #Stop criterium 1 - Function Value
    StopPointsDifference = stop2_Box.get()                                           #Stop criterium 2 - Points Difference

    L = IterationsVar
    intervalLength = RangeVar
    accFX = StopFunctionValue
    accX = StopPointsDifference

    initialPoint = [4.5, -1]
    initialPoint = []
    strInitialPoint = StartPointVar
    strInitialPoint = strInitialPoint.replace("[" , "")
    strInitialPoint = strInitialPoint.replace("]" , "")

    list = strInitialPoint.split(",")
    #print(list)
    for i in range(len(list)):
        initialPoint.append(float(list[i]))

    #print("Initial point: ")
    #print(initialPoint)
    #print("Initial point: ")
    #print(len(initialPoint))


############################### Charts ########################################


def f(X,Y):         #Preparing for plotting

    global f
    global Z
    global tmp

    feature_x = np.linspace(-10.0, 10.0, 1000)
    feature_y = np.linspace(-10.0, 10.0, 1000)

    # Creating 2-D grid of features

    [X, Y] = np.meshgrid(feature_x, feature_y)

    #FunctionVar = FunctionVar.replace("math", "np")
    f1 = eval(FunctionVar.replace("math", "np"))
    Z = []
    tmp = []
    Z.append(f1)
    print(f1)

    for e1 in Z:
        for e2 in e1:
            tmp.append(e2)


##############Test3D

def Prepare3DData(X,Y):

    global Value3DFunction
    #print("FKJDKHF")
    #print(FunctionVar)
    expression = FunctionVar.replace("math", "np")
    #print(expression)
    Value3DFunction = eval(expression)

    return Value3DFunction


#def plotContourf():



def plot2D():
    feature_x = np.linspace(-10.0, 10.0, 1000)
    feature_y = np.linspace(-10.0, 10.0, 1000)

    [X, Y] = np.meshgrid(feature_x, feature_y)

    fig, ax = plt.subplots(1, 1)

    f(X,Y)

    ax.clear()
    chart = ax.contourf(X, Y, tmp, levels=30)

    ax.set_title('Contour Plot')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.colorbar(chart)

    ######################## Creating points, tutaj mozesz dorzuciÄ‡ te punkty kolejne ########################

    #print("List:",pointList)

    newList = []

    for i in range(len(pointList)-1):
        newList.append(pointList[i])
        x = pointList[i+1][0]
        p = [x,pointList[i][1]]
        newList.append(p)

    #print("lista",newList)


    RemoveFirstLast = pointList[1:-1]

    #print("ssds",RemoveFirstLast)

    data = np.array(newList)                #
    pointx, pointy = data.T                 #

    #print("dada",len(data))
    #print("la:", data)
    #print("lalala:",data.T)


    newList2 = newList                      #
    newList2.append(pointList[-1])          #

    dataLine = np.array(newList)            #
    pointxLine, pointyLine = dataLine.T     #

    plt.scatter(pointx,pointy,s=10,color='blue')
    plt.plot(pointxLine,pointyLine,linestyle = ':')                             #Punkty przejĹ›ciowe

    FirstElem = pointList[0]
    #print("first",FirstElem)
    dataFirstElem = np.array(FirstElem)
    FirstPointx, FirstPointy = dataFirstElem.T
    plt.scatter(FirstPointx, FirstPointy,s=10, color='black')  # Punkt poczÄ…tkowy


    LastElem = pointList[-1]
    dataLastElem = np.array(LastElem)
    LastPointx, LastPointy = dataLastElem.T
    plt.scatter(LastPointx,LastPointy,s=10,color='red')      #Punkt koĹ„cowy

    plt.show()

    pointList.clear()
    RemoveFirstLast.clear()


def plot3D():

    #X=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
    #Y=X

    X = np.linspace(-5.0, 5.0, 100)
    Y = np.linspace(-5.0, 5.0, 100)
    X,Y=np.meshgrid(X,Y)

    Prepare3DData(X, Y)

    fig = plt.figure()
    axes = fig.gca(projection="3d")

    axes.plot_surface(X,Y,Value3DFunction,cmap="viridis")

    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_zlabel('Z')
    axes.set_title('3D Plot')

    plt.contour(X,Y,Value3DFunction,cmap="viridis")
    plt.show()


def plotAll():

    plot2D()
    plot3D()

def Results():      # draw charts and calculate results

    DownloadParameters()
    global pointList
    global optPlace
    global optValue

####### Czyszczenie rezultatów w GUI #########

    optPlace = "                                                                                                                                 "
    optValue = "                                                                                                                                 "

    FunctionValueLabel = Label(root, text=optValue)
    FunctionValueLabel.place(x=700, y=150)

    MinimumLabel = Label(root, text=optPlace)
    MinimumLabel.place(x=700, y=200)

####### Czyszczenie rezultatów w GUI #########

    #accX = 10**(-3)
    #accFX = 10**(-3)
    algorithm = OptimizationAlgorithm(givenExpression, L, initialPoint, intervalLength, accX, accFX)
    #pointList = algorithm.runAlgorithm()
    results = algorithm.runAlgorithm()
    pointList = results[0]
    calculationLogs = results[1]
    optPlace = pointList[-1]
    optValue = OptimizationAlgorithm.functionExample(givenExpression, optPlace)
    print("GUI:")
    print(calculationLogs)
    optValue = float(f'{optValue:.4f}')

    FunctionValueLabel = Label(root, text=optValue)
    FunctionValueLabel.place(x=700, y=150)

    optPlace[0] = float(f'{optPlace[0]:.4f}')
    optPlace[1] = float(f'{optPlace[1]:.4f}')

    MinimumLabel = Label(root, text=optPlace)
    MinimumLabel.place(x=700, y=200)

    ############# Poszczególne kroki

    text_scroll = Scrollbar


    Steps = ScrolledText(root)
    Steps.config(width=50, height=10, wrap=NONE)
    Steps.insert(END,calculationLogs)
    Steps.place(x=700,y=250)
    h = Scrollbar(root, orient='horizontal')
    h.place(x=700, y=414, width=420)
    h.config(command=Steps.xview)
    #StepsLabel = Label(root, text=Steps,yscrollcomand=text_scroll.set)
    #StepsLabel.place(x=700, y=250)


    plotAll()  # !!!!!!!!!!!!!!


################ Buttony ####################

AcceptButton = Button(root, text="Accept function and parameters",command=play)
AcceptButton.place(x=300,y=500)

#Clear Button

ClearButton = Button(root, text="Clear",command=clear)
ClearButton.place(x=630,y=500)

#Calculate Button - tutaj w sumie do zrobienia, ale trzeba by wrzuciÄ‡ jakÄ…Ĺ› funkcje tutaj, ktĂłra by startowaĹ‚a po prostu, narazie rysuje wykresy

CalculateButton = Button(root, text="Calculate",command=Results)
CalculateButton.place(x=850, y=500)



root.mainloop()