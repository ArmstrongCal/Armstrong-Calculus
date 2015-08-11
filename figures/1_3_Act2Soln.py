from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("1_3_Act2Soln", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -8, 2.5, 40])

xrange = [-0.5,0.5,2.5]
yrange = [-8,8,40]

grid = Grid(xrange, yrange)
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,0.5,2]) 
axes.setvticks([0,8,32])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0,1,2],[0,16,40])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label("$t$", [2.3, 2])
label.draw()

label = Label("$y$", [0.1, 36])
label.draw()

label = Label("secant line", [0.9, 38])
label.setscale(0.8)
label.draw()

label = Label("tangent line", [1.6, 23])
label.setscale(0.8)
label.draw()

def f(x):
    return -16*x*x+16*x+32

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,2])
graph.draw()

def g(x):
    return f(1) + (f(2)-f(1))/(2-1)*(x-1)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([0.2,2.8])
graph.draw()

a = 1
dx = 0.8
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([1, f(1)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([2, f(2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

endfigure()
