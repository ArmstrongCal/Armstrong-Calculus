from figures import *
from defaults import *

width = 110
height = 110

beginfigure("1_8_Options", 4*width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -2, 4, 4])

grid = Grid([-2, 1, 4], [-2, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 1 + 0.5*(x-1)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,3])
graph.draw()

def f(x):
    return 1 + 0.5*(x-1) + 0.25*(x-1)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1.5,3.5])
graph.draw()

point = Point([1, 1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()

restore()

save()
margin = 5
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-2, -2, 4, 4])

grid = Grid([-2, 1, 4], [-2, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 1 + 0.5*(x-1)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,3])
graph.draw()

def f(x):
    return 1 + 0.5*(x-1) - 0.25*(x-1)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1.5,3.5])
graph.draw()

point = Point([1, 1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


restore()

save()
margin = 5
setupcoordinates([2*width+margin, margin, 3*width-margin, height-margin],
                 [-2, -2, 4, 4])

grid = Grid([-2, 1, 4], [-2, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 1 + 0.5*(x-1)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,3])
graph.draw()

def f(x):
    return 1 + 0.5*(x-1) - 0.25*(x-1)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1.5,1])
graph.draw()

def f(x):
    return 1 + 0.5*(x-1) + 0.25*(x-1)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,3.5])
graph.draw()

point = Point([1, 1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


restore()
save()
margin = 5
setupcoordinates([3*width+margin, margin, 4*width-margin, height-margin],
                 [-2, -2, 4, 4])

grid = Grid([-2, 1, 4], [-2, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 1 + 0.5*(x-1)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,3])
graph.draw()

def f(x):
    return 1 + 0.5*(x-1) + 0.25*(x-1)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1.5,1])
graph.draw()

def f(x):
    return 1 + 0.5*(x-1) - 0.25*(x-1)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,3.5])
graph.draw()

point = Point([1, 1], 2)
point.setfillcolor(pointcolor)
point.fill()
point.draw()


restore()


endfigure()
