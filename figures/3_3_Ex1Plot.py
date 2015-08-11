from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_3_Ex1Plot", width, height)

save()
margin = 15
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, 0, 25, 30])

grid = Grid([-5, 5, 25], [0, 5, 30])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 5, 20])
axes.setvticks([0, 5, 25])
axes.drawticks()

axes.setlabels([0, 5, 20], [0, 5, 25])
axes.drawlabels()

label = Label("$y=A(x)$", [18,13])
label.draw()

def f(x):
    return 0.04811252245*x**2+(5.0-.25*x)**2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,20])
graph.draw()

def f(x):
    return 0.04811252245*x**2+(5.0-.25*x)**2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-5,0])
graph.draw()

def f(x):
    return 0.04811252245*x**2+(5.0-.25*x)**2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([20,25])
graph.draw()

point = Point([0, f(0)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([20, f(20)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([11.3007, f(11.3007)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


restore()

endfigure()
