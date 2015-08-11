from figures import *

width = 200
height = 200
beginfigure("example3", width, height)

save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], [-1,-1,1,1])

grid = Grid([-1,0.25, 1], [-1,0.25,1], color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

import math
curve = ParametricCurve(Function(lambda t: math.cos(t)),
                        Function(lambda t: math.sin(3*t)),
                        [0, 2*math.pi], color = blue, linewidth = 2)
curve.draw()

ellipse = Ellipse([0, 0.25], [0.25, 0.5], fillcolor = lightred, color =red)
ellipse.fill()
ellipse.draw()

circle = Circle([0,-0.5], 0.25, fillcolor = lightgreen, color = green)
circle.fill()
circle.draw()

restore()
endfigure()
