from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_4_Crock", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -5, 3, 1])

grid = Grid([-3, 6, 3], [-5, 6, 1])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 5, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-1.05, 1.05, 0])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [0, 2, 6])
#axes.drawlabels()

line = Line([0.75,-4],[1.5,0], color=darkblue, linewidth = 1)
line.draw()

line = Line([-0.75,-4],[-1.5,0], color=darkblue, linewidth = 1)
line.draw()

import math
curve = ParametricCurve(Function(lambda t: 0.75*math.cos(t)),
                        Function(lambda t: 0.125*math.sin(t)-4),
                        [1*math.pi, 2*math.pi], color = darkblue, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 1.5*math.cos(t)),
                        Function(lambda t: 0.25*math.sin(t)),
                        [0*math.pi, 2*math.pi], color = darkblue, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 1.3333333*math.cos(t)),
                        Function(lambda t: 0.175*math.sin(t)-1),
                        [0*math.pi, 2*math.pi], color = blue, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 1.3333333*math.cos(t)),
                        Function(lambda t: 0.175*math.sin(t)-1.25),
                        [1*math.pi, 2*math.pi], color = blue, linewidth = 1)
curve.draw()

line = Line([1.3333333,-1],[1.3333333,-1.25], color=blue, linewidth = 1)
line.draw()

line = Line([-1.3333333,-1],[-1.3333333,-1.25], color=blue, linewidth = 1)
line.draw()


point = Point([0.75,-4], size = 1.5, fillcolor=pointcolor)
point.fill()
point.draw()

point = Point([1.5,0], size = 1.5, fillcolor=pointcolor)
point.fill()
point.draw()

label = Label(r"$x^+$", [0.1,-4.5], alignment = "lc", offset = [2, 0] )
label.draw()

label = Label(r"$y^+$", [2.25,0], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$(0,1.5)$", [1.5,0], alignment = "lt", offset = [2, -4], scale=0.8  )
label.draw()

label = Label(r"$(4,0.75)$", [0.75,-4], alignment = "lb", offset = [4, 2], scale=0.8 )
label.draw()

label = Label(r"$\triangle x$", [-1.3333333,-1.125], alignment = "rc", offset = [-2, 0] )
label.draw()

label = Label(r"$x$", [0,-1.0], alignment = "rc", offset = [-2, 0] )
label.draw()

label = Label(r"$y=f(x)$", [1.25,-2], alignment = "lc", offset = [2, 0], scale=0.8 )
label.draw()


restore()

endfigure()
