from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_1_IntWRTy", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1.5, -2, 3.5, 3])

grid = Grid([-1.5, 5, 3.5], [-2, 5, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 2])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [-1, 1, 2])
axes.drawlabels()

import math
f = Function(lambda x:math.sqrt(x+1))
g = Function(lambda x:-1*math.sqrt(x+1))
h = Function(lambda x:x-1)

area = AreaBetweenCurves(f, g, fillcolor = magenta, domain=[-0.9999,0])
area.fill()
area.draw()

area = AreaBetweenCurves(f, h, fillcolor = magenta, domain=[0,3])
area.fill()
area.draw()

line = Line([0,-1],[0,1], color=magenta, linewidth = 2)
line.draw()

graph = Graph(f, domain=[-0.9999,3.5], color = red, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(g, domain=[-0.9999,1], color = red, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(h, color = blue, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

label = Label(r"$x=y^2-1$", [1,2], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$y=x-1$", [1.5,0.5], alignment = "lt", offset = [2,-2])
label.draw()

restore()

########

save()

setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-1.5, -2, 3.5, 3])

grid = Grid([-1.5, 5, 3.5], [-2, 5, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 2])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [-1, 1, 2])
axes.drawlabels()

import math
f = Function(lambda x:math.sqrt(x+1))
g = Function(lambda x:-1*math.sqrt(x+1))
h = Function(lambda x:x-1)


graph = Graph(f, domain=[-0.9999,3.5], color = red, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(g, domain=[-0.9999,1], color = red, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(h, color = blue, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

rs = RiemannSum(f, 1, g, 
                domain = [-0.6,-0.4], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()

rs = RiemannSum(f, 1, h, 
                domain = [1.1,1.3], fillcolor = boxcolor,
                style = RiemannSum.MID) 
                               # RiemannSum(f, g, 10) makes the boxes
                               #   between the graphs of f and g
rs.fill()
rs.draw()


label = Label(r"$x=y^2-1$", [1,2], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$y=x-1$", [0.5,-0.5], alignment = "lt", offset = [2,-2])
label.draw()

restore()

########

save()

setupcoordinates([2*width+margin, margin, 3*width-margin, height-margin],
                 [-1.5, -2, 3.5, 3])

grid = Grid([-1.5, 5, 3.5], [-2, 5, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 2])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [-1, 1, 2])
axes.drawlabels()

import math
f = Function(lambda x:math.sqrt(x+1))
g = Function(lambda x:-1*math.sqrt(x+1))
h = Function(lambda x:x-1)


graph = Graph(f, domain=[-0.9999,3.5], color = red, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(g, domain=[-0.9999,1], color = red, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

graph = Graph(h, color = blue, linewidth = graphwidth)
cliptoboundingbox()
graph.draw()

p = [-0.5,0.6]
q = [1.7,0.6]
r = [1.7,0.8]
s = [-0.5,0.8]

points = [p,q,r,s]
pgram = Polygon(points = points, color = black, fillcolor = boxcolor, linewidth = 1, closed = True)
pgram.setmiterlimit(1)
pgram.fill()
pgram.draw()


label = Label(r"$x=y^2-1$", [1,2], alignment = "lb", offset = [2,2])
label.draw()

label = Label(r"$x = y+1$", [0.5,-0.5], alignment = "lt", offset = [2,-2])
label.draw()

label = Label(r"$\triangle y$", [1.7,0.7], alignment = "lc", offset = [2,0])
label.draw()

restore()


endfigure()
