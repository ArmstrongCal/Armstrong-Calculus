from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("4_2_Act2Soln", width, height)

# start left figure
save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -1, 6, 6])

grid = Grid([-1,7,6], [-1,7,6], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([2,3,5], [2,2,4])
axes.drawticks()

axes.sethlabels([2,3,5])
axes.drawhlabels()
axes.setvlabels([2,2,4])
axes.drawvlabels()

import math
f = Function(lambda x: 0.2222*(x-3)**2+2)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[2,5])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = v(t)$", [0.2,4], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
