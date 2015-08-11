from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("4_3_AdditiveProp", width, height)

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
f = Function(lambda x: 1*math.sin(2*x)+1*x)
a = 0.2
b = 1
c = 2.4

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[a,b])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[b,c])
area.fill()
area.draw()

cliptoboundingbox()
graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = f(x)$", [0.1,2], alignment = "lb", offset = [2, 2] )
label.draw()


label = Label(r"$A_1$", [0.6,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_2$", [1.6,0.5], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$a$", [a,-0.4], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$b$", [b,-0.4], alignment = "cb", offset = [0, 2] )
label.draw()

label = Label(r"$c$", [c,-0.4], alignment = "cb", offset = [0, 2] )
label.draw()

restore()


endfigure()
