from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_2_PA1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -4, 6, 4])

grid = Grid([-1, 7, 6], [-4, 8, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 5, 5]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 3, 3])
axes.drawticks()

axes.setlabels([0, 5, 5], # you can do this separately with seth(v)labels
               [0, 3, 3])
axes.drawlabels()

line = Line([0,3],[5,0], color=darkblue, linewidth = 1)
line.draw()

line = Line([0,-3],[5,0], color=darkblue, linewidth = 1)
line.draw()

import math
curve = ParametricCurve(Function(lambda t: 0.4*math.cos(t)),
                        Function(lambda t: 3*math.sin(t)),
                        [0.5*math.pi, 1.5*math.pi], color = darkblue, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.4*math.cos(t)+0.8),
                        Function(lambda t: 2.4*math.sin(t)),
                        [0.5*math.pi, 1.5*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.4*math.cos(t)+1.2),
                        Function(lambda t: 2.4*math.sin(t)),
                        [0*math.pi, 12*math.pi], color = red, linewidth = 1)
curve.draw()

line = Line([0.8,2.4],[1.2,2.4], color=red, linewidth = 1)
line.draw()

line = Line([0.8,-2.4],[1.2,-2.4], color=red, linewidth = 1)
line.draw()


label = Label(r"$\triangle x$", [1.1,-2.9], alignment = "cc", offset = [0,0] )
label.draw()

line = Line([1.2,-0.2],[1.2,0.2], color=black, linewidth = 1)
line.draw()

label = Label(r"$x$", [1.2,-0.4], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$y$", [0.1,3.3], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$y=f(x)$", [3.1,1], alignment = "lb", offset = [3, 4] )
label.draw()

restore()

endfigure()
