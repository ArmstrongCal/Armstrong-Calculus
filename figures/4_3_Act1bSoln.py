from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("4_3_Act1bSoln", width, height)

# start left figure
save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-2, -8, 5, 8])

grid = Grid([-2,7,5], [-8,16,8], color = gridcolor)
grid.setlinewidth = gridwidth
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([-1,1,4], [0,3,2])
axes.drawticks()

import math
f = Function(lambda x:2-2*x)

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[-1,1])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[1,4])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
graph.draw()

label = Label(r"$y = 2-2x$", [3,-4], alignment = "rt", offset = [-2, -2] )
label.draw()


label = Label(r"$A_1$", [-0.2,1], alignment = "cc", offset = [0, 0] )
label.draw()

label = Label(r"$A_2$", [3,-2], alignment = "cc", offset = [0, 0] )
label.draw()

p1 = Point([-1,4], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$(-1,4)$", [-1,4], alignment = "lb", offset = [2,2] )
label.draw()

p1 = Point([1,0], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$(1,0)$", [1,0], alignment = "lb", offset = [2,2] )
label.draw()

p1 = Point([4,-6], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

label = Label(r"$(4,-6)$", [4,-6], alignment = "rt", offset = [-2,-2] )
label.draw()



restore()


endfigure()
