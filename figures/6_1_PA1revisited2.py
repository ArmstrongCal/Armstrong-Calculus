from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_1_PA1revisited2", 2*width, height)

margin = 10

########

save()

setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -1, 4, 8])

grid = Grid([-0.5, 4.5, 4], [-1, 9, 8])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1.25, 1.25]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 8, 6])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [0, 2, 6])
#axes.drawlabels()

import math
f = Function(lambda x:x**2-2*x+2)
g = Function(lambda x:x+2)

graph = Graph(f, color = blue, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(g, color = red, linewidth = 1)
graph.draw()

rs = RiemannSum(f, 1, g, 
                domain = [1.1,1.4], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()



label = Label("$g$", [0.25, 2.5], alignment = "lb", offset = [2,2])
label.draw()

label = Label("$f$", [0.25, 0.2], alignment = "lb", offset = [2,2])
label.draw()

label = Label("$x$", [1.25, -0.9], alignment = "cb", offset = [0,2])
label.draw()

label = Label(r"$\triangle x$", [1.25, 0], alignment = "cb", offset = [0,2])
label.draw()

label = Label(r"$g(x)-f(x)$", [1.5, 2.35], alignment = "lc", offset = [2,0])
label.draw()

restore()

########

save()

setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-0.5, -1, 4, 8])

grid = Grid([-0.5, 4.5, 4], [-1, 9, 8])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 2, 6])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [0, 2, 6])
axes.drawlabels()

import math
f = Function(lambda x:x**2-2*x+2)
g = Function(lambda x:x+2)

area = AreaBetweenCurves(g, f, fillcolor = magenta, domain=[0,3])
area.fill()
area.draw()

graph = Graph(f, color = blue, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(g, color = red, linewidth = graphwidth)
graph.draw()

label = Label("$f$", [0.25, 0.3], alignment = "lb", offset = [2,2])
label.draw()

label = Label("$g$", [0.25, 2.5], alignment = "lb", offset = [2,2])
label.draw()

restore()


endfigure()
