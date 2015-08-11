from figures import *

width = 200
height = 200
beginfigure("example5", 2*width, height)

# start left figure
save()
margin = 5
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-1, -1, 7, 2])

grid = Grid([-1,1, 7], [-1,0.5,2], color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([-1,1,7], [-1,0.5, 2])
axes.drawticks()

import math
f = Function(lambda x:math.cos(x)+0.5)
a = f.solve(2)
x0 = 3.7

area = AreaBetweenCurves(f, fillcolor = lightblue, domain=[0,a])
area.fill()
area.draw()

area = AreaBetweenCurves(f, fillcolor = lightred, domain=[a,x0])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = 2)
graph.draw()

#end left figure
restore()

#start right figure
save()
setupcoordinates([200+margin,margin,200+width-margin,height-margin], 
                 [-1, -1, 7, 2])

grid = Grid([-1,1, 7], [-1,0.5,2], color = lightgray)
grid.draw()

axes = Axes()
axes.draw()

axes.setticks([-1,1,7], [-1,0.5, 2])
axes.drawticks()

fprime = f.differentiate()
graph = Graph(fprime, color = lightgreen, linewidth = 2)
graph.draw()

save()
cliptoboundingbox()
fint = f.antidifferentiate(0)
graph = Graph(fint, color = blue, linewidth = 2)
graph.draw()
restore()

restore()

endfigure()
