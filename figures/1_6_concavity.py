from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_6_concavity", 2*width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 3, 3])

grid = Grid([-1, 1, 3], [-1, 1, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 0.5*(x-1)**2 + 0.5

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-0.8,2.8])
graph.draw()

a = -0.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([-0.5,f(-0.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

a = 0.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([0.5,f(0.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

a = 1.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([1.5,f(1.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

a = 2.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([2.5,f(2.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()

save()
margin = 10
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-1, -1, 3, 3])

grid = Grid([-1, 1, 3], [-1, 1, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 2.5 - 0.5*(x-1)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-0.8,2.9])
graph.draw()

a = -0.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([-0.5,f(-0.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

a = 0.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([0.5,f(0.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

a = 1.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([1.5,f(1.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

a = 2.5
dx = 0.4
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

p1 = Point([2.5,f(2.5)], 2)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()


restore()

endfigure()
