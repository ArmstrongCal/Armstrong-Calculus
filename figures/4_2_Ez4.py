from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("4_2_Ez4", width, height)

# start left figure
save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -1, 5, 5])

grid = Grid([-1,0.5,5], [-1,0.5,5], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,4], [0,1,4])
axes.drawticks()

axes.sethlabels([0,1,4])
axes.drawhlabels()
axes.setvlabels([0,1,4])
axes.drawvlabels()

import math
f = Function(lambda x:0.5*math.exp(0.5*x))

graph = Graph(f, color = blue, linewidth = graphwidth, domain = [0,4])
graph.draw()

label = Label(r"$y = r(t)$", [3.5,3], alignment = "rb", offset = [-2, 2] )
label.draw()

label = Label(r"weeks", [4,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"tons/week", [0.25,4], alignment = "lb", offset = [2, 2] )
label.draw()


label.draw()

restore()

endfigure()
