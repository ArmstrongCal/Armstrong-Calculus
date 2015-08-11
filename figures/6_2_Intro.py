from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_2_Intro", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -3, 4, 3])

grid = Grid([-1, 5, 4], [-3, 6, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 3, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 2, 2])
axes.drawticks()

axes.setlabels([0, 3, 3], # you can do this separately with seth(v)labels
               [0, 2, 2])
axes.drawlabels()

line = Line([0,2],[3,2], color=darkblue, linewidth = 1)
line.draw()

line = Line([0,-2],[3,-2], color=darkblue, linewidth = 1)
line.draw()

import math
curve = ParametricCurve(Function(lambda t: 0.2*math.cos(t)),
                        Function(lambda t: 2*math.sin(t)),
                        [0.5*math.pi, 1.5*math.pi], color = darkblue, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.2*math.cos(t)+3),
                        Function(lambda t: 2*math.sin(t)),
                        [0*math.pi, 2*math.pi], color = darkblue, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.2*math.cos(t)+1),
                        Function(lambda t: 2*math.sin(t)),
                        [0.5*math.pi, 1.5*math.pi], color = red, linewidth = 1)
curve.draw()

curve = ParametricCurve(Function(lambda t: 0.2*math.cos(t)+1.2),
                        Function(lambda t: 2*math.sin(t)),
                        [0*math.pi, 2*math.pi], color = red, linewidth = 1)
curve.draw()

line = Line([1,2],[1.2,2], color=red, linewidth = 1)
line.draw()

line = Line([1,-2],[1.2,-2], color=red, linewidth = 1)
line.draw()


line = Line([1.2,-0.1],[1.2,0.1], color=black, linewidth = 1)
line.draw()

label = Label(r"$\triangle x$", [1.1,-2.3], alignment = "cc", offset = [0,0] )
label.draw()


label = Label(r"$x$", [1.2,-0.4], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$y$", [0.1,2.5], alignment = "lb", offset = [2, 2] )
label.draw()


restore()

endfigure()
