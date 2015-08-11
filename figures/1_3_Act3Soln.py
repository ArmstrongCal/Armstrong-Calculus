from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_3_Act3Soln", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -20, 5, 100])

xrange = [-1,1,5]
yrange = [-20,20,100]

grid = Grid([-1,6,5], [-20,120,100])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,4]) 
axes.setvticks([0,20,80])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0,1,4],[0,20,80])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label("$t$ (decades)", [3.1, 5])
label.draw()

label = Label("$y$ (in thousands)", [0.3, 90])
label.draw()

label = Label("$P$", [4.0, 70])
label.draw()

def f(x):
    return 25*math.exp(0.2*x)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,5])
graph.draw()

def g(x):
    return f(2) + (f(4)-f(2))/(4-2)*(x-2)

graph = Graph(Function(g))
graph.setcolor(magenta)
graph.setlinewidth(graphwidth)
graph.setdomain([1.2,4.8])
graph.draw()

a = 2
dx = 1.5
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([4, f(4)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

point = Point([2, f(2)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

endfigure()
