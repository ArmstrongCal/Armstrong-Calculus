from figures import *
from defaults import *

width = 120
height = 120

beginfigure("3_1_2Dtest", 4*width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

grid = Grid([-1, 6, 5], [-1, 6, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

def f(x):
    return -0.5*(x-2)**2 + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

a = 2
dx = 1.2
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

### Fig 2

save()

margin = 5
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

grid = Grid([-1, 6, 5], [-1, 6, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

def f(x):
    return 0.5*(x-2)**2 + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

a = 2
dx = 1.2
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

### Fig 3

save()

margin = 5
setupcoordinates([2*width+margin, margin, 3*width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

grid = Grid([-1, 6, 5], [-1, 6, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

def f(x):
    return 0.5*(x-2)**3 + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

a = 2
dx = 1.2
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

### Fig 4

save()

margin = 5
setupcoordinates([3*width+margin, margin, 4*width-margin, height-margin],
                 [-1, -1, 5, 5])

axes = Axes()
axes.draw()

grid = Grid([-1, 6, 5], [-1, 6, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

def f(x):
    return -0.5*(x-2)**3 + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,5])
graph.draw()

a = 2
dx = 1.2
tangentline = Function(f).tangentline(a)
tangent = Graph(tangentline)
tangent.setdomain([a-dx, a+dx])
tangent.setlinewidth(graphwidth)
tangent.setcolor(tangentlinecolor)
tangent.draw()

point = Point([a, f(a)], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

endfigure()
