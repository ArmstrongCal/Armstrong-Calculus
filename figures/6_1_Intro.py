from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_1_Intro", width, height)

# start left figure
save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -1, 3, 3])

grid = Grid([-1,4,3], [-1,4,3], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

import math
f = Function(lambda x:0.5*math.cos(2.5*x)+2)
a = 0.25
b = 2.5

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[a,b])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = f(x)$", [0.1,2.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$a$", [a,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$b$", [b,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$A = \int_a^b f(x) \, dx$", [1.35,1], alignment = "cc", offset = [0, 0] )
label.draw()


restore()

endfigure()
