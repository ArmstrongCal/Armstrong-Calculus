from figures import *
from defaults import *

width = 1.5*standardwidth
height = 1.5*standardheight
beginfigure("6_2_Ex4", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1.5, -3.5, 3.5, 1.5])

grid = Grid([-1.5, 5, 3.5], [-3.5, 5, 1.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([-3, 1, 1])
axes.drawticks()

axes.setlabels([0, 1, 1], # you can do this separately with seth(v)labels
               [-2, 3, 1])
axes.drawlabels()

import math
f = Function(lambda x:x)
g = Function(lambda x:x**2)

area = AreaBetweenCurves(f, g, fillcolor = lightgray, domain=[0,1])
area.fill()
area.draw()

f = Function(lambda x:-1*x-2)
g = Function(lambda x:-1*x**2-2)

area = AreaBetweenCurves(f, g, fillcolor = lightgray, domain=[0,1])
area.fill()
area.draw()

def f(x):
    return x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setdomain([0,1])
graph.setmiterlimit(1)
graph.draw()

def f(x):
    return -1*x-2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setdomain([0,1])
graph.setmiterlimit(1)
graph.draw()

def f(x):
    return x**2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkgreen)
graph.setdomain([0,1])
graph.setmiterlimit(1)
graph.draw()

def f(x):
    return -1*x**2-2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkgreen)
graph.setdomain([0,1])
graph.setmiterlimit(1)
graph.draw()

import math

curve = ParametricCurve(Function(lambda t: 0.1*math.cos(t)+0.4),
                        Function(lambda t: 1.5*math.sin(t)-1),
                        [0.5*math.pi, 1.5*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.1*math.cos(t)+0.6),
                        Function(lambda t: 1.5*math.sin(t)-1),
                        [0*math.pi, 2*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.05*math.cos(t)+0.6),
                        Function(lambda t: 1.25*math.sin(t)-1),
                        [0*math.pi, 2*math.pi], color = magenta, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.1*math.cos(t)+1.02),
                        Function(lambda t: 2.02*math.sin(t)-1),
                        [0*math.pi, 2*math.pi], color = darkblue, linewidth = 1)
curve.draw()

line = Line([-1,-1],[3,-1], color=black, linewidth = 1, dash=[2,2])
line.draw()

line = Line([1.5,-1],[1.5,0.25], color=magenta, linewidth = 1)
line.draw()

label = Label(r"$r(x)$", [1.5,-0.5], alignment = "lb", offset = [2,2])
label.draw()

line = Line([2.1,-1],[2.1,0.5], color=red, linewidth = 1)
line.draw()

label = Label(r"$R(x)$", [2.1,-0.4], alignment = "lb", offset = [2,2])
label.draw()


line = Line([0.4,0.5],[0.6,0.5], color=red, linewidth = 1)
line.draw()

line = Line([0.4,-2.5],[0.6,-2.5], color=red, linewidth = 1)
line.draw()





restore()

endfigure()
