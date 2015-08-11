from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("4_2_Intro", width, height)

# start left figure
save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -1, 3, 2])

grid = Grid([-1,4,3], [-1,3,2], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([0,1,2], [0,1,2])
#axes.drawticks()

import math
f = Function(lambda x:math.cos(2.5*x)+0.5)
a = f.solve(1)
b = f.solve(1.7)
x0 = 2.8

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0.2,a])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[a,b])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[b,x0])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = v(t)$", [0.1,1.5], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label(r"$a$", [0.2,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$b$", [x0,-0.35], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$A_1$", [0.42,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_2$", [1.25,-0.2], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_3$", [2.35,0.5], alignment = "cc", offset = [0, 0] )
label.draw()


restore()

endfigure()
