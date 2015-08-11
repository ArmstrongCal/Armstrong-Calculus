from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_2_Ex1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -5, 3, 5])

grid = Grid([-3, 6, 3], [-5, 10, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2, 2, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([-4, 2, 4])
axes.drawticks()

axes.setlabels([0, 2, 2], # you can do this separately with seth(v)labels
               [0, 4, 4])
axes.drawlabels()

def f(x):
    return 4-x**2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setdomain([-2,2])
graph.draw()

def f(x):
    return -(4-x**2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setdomain([-2,2])
graph.draw()

import math

curve = ParametricCurve(Function(lambda t: 0.4*math.cos(t)-1.2),
                        Function(lambda t: 3*math.sin(t)),
                        [0.5*math.pi, 1.5*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.4*math.cos(t)-0.8),
                        Function(lambda t: 3*math.sin(t)),
                        [0*math.pi, 2*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.5*math.cos(t)),
                        Function(lambda t: 4*math.sin(t)),
                        [0.5*math.pi, 1.5*math.pi], color = darkblue, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.5*math.cos(t)),
                        Function(lambda t: 4*math.sin(t)),
                        [-0.5*math.pi, 0.5*math.pi], color = lightblue, linewidth = 1, dash = [1,1])
curve.draw()

line = Line([-1.2,3],[-0.8,3], color=red, linewidth = 1)
line.draw()

line = Line([-1.2,-3],[-0.8,-3], color=red, linewidth = 1)
line.draw()


label = Label(r"$\triangle x$", [-1,-3.5], alignment = "cc", offset = [0,0] )
label.draw()

line = Line([-1,-0.2],[-1,0.2], color=black, linewidth = 1)
line.draw()

label = Label(r"$x$", [-1,-0.7], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$y$", [0.1,4.3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y=4-x^2$", [0.5,3.5], alignment = "lb", offset = [3, 4] )
label.draw()

restore()

endfigure()
