from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_2_Ex3", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1.5, -1.5, 1.5, 1.5])

grid = Grid([-1.5, 3, 1.5], [-1.5, 3, 1.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 1])
axes.drawticks()

axes.setlabels([0, 1, 1], # you can do this separately with seth(v)labels
               [0, 1, 1])
axes.drawlabels()

import math
f = Function(lambda x:math.sqrt(x))
g = Function(lambda x:x**4)

area = AreaBetweenCurves(f, g, fillcolor = lightgray, domain=[0,1])
area.fill()
area.draw()

#1
f = Function(lambda x:math.sqrt(math.fabs(x)))
g = Function(lambda x:x**4)

area = AreaBetweenCurves(f, g, fillcolor = lightgray, domain=[-1,0])
area.fill()
area.draw()

def f(x):
    return math.sqrt(x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkgreen)
graph.setdomain([0,1])
graph.draw()

#2 
def f(x):
    return math.sqrt(math.fabs(x))

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkgreen)
graph.setdomain([-1,0])
graph.draw()


def f(x):
    return x**4

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setdomain([0,1])
graph.draw()

def f(x):
    return x**4

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setdomain([-1,0])
graph.draw()


################

import math

curve = ParametricCurve(Function(lambda t: 0.8409*math.cos(t)),
                        Function(lambda t: 0.1*math.sin(t)+0.4),
                        [1*math.pi, 2*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.8409*math.cos(t)),
                        Function(lambda t: 0.1*math.sin(t)+0.6),
                        [0*math.pi, 2*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.32*math.cos(t)),
                        Function(lambda t: 0.04*math.sin(t)+0.6),
                        [0*math.pi, 2*math.pi], color = magenta, linewidth = 1)
curve.draw()


curve = ParametricCurve(Function(lambda t: 1*math.cos(t)),
                        Function(lambda t: 0.1*math.sin(t)+1),
                        [0*math.pi, 2*math.pi], color = darkblue, linewidth = 1)
curve.draw()

line = Line([0.8409,0.4],[0.8409,0.6], color=red, linewidth = 1)
line.draw()

line = Line([-0.8409,0.4],[-0.8409,0.6], color=red, linewidth = 1)
line.draw()


label = Label(r"$\triangle y$", [1.1,0.5], alignment = "cc", offset = [0,0] )
label.draw()

label = Label(r"$x=\sqrt[4]{y}$", [1,0.8], alignment = "lb", offset = [2, 2] )
#label.draw()

restore()

#######

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 8, 4], [-4, 8, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

circle = Circle([0,0], 3, fillcolor = lightgray, color = red)
circle.fill()
#circle.draw()

circle = Circle([0,0], 1, fillcolor = emptypoint, color = magenta)
circle.fill()
#circle.draw()


curve = ParametricCurve(Function(lambda t: 3*math.cos(t)),
                        Function(lambda t: 3*math.sin(t)),
                        [0*math.pi, 2*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 1*math.cos(t)),
                        Function(lambda t: 1*math.sin(t)),
                        [0*math.pi, 2*math.pi], color = magenta, linewidth = 1)
curve.draw()

line = Line([0,0],[1,0], color=black, linewidth = 1)
line.draw()

line = Line([0,0],[3*math.sqrt(2)/2,3*math.sqrt(2)/2], color=black, linewidth = 1)
line.draw()

label = Label(r"$r(y)$", [0.5,-0.75], alignment = "cb", offset = [0,2], scale = 0.8 )
label.draw()

label = Label(r"$R(y)$", [3*math.sqrt(2)/4,3*math.sqrt(2)/4], alignment = "lt", offset = [2,-2], scale=0.8 )
label.draw()

restore()


endfigure()
