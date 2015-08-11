from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("4_3_TrapArea", width, height)

# start left figure
save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -2, 5, 11])

grid = Grid([-1,6,5], [-2,13,11], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,4], [3,2,9])
axes.drawticks()

axes.sethlabels([1,3,4])
axes.drawhlabels()
axes.setvlabels([3,6,9])
axes.drawvlabels()

import math
f = Function(lambda x:2*x+1)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[1,4])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$f(x) = 2x+1$", [4,9], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"$\int_1^4 (2x+1) \, dx$", [2.5,2], alignment = "cc", offset = [0,0] )
label.draw()

restore()

endfigure()
