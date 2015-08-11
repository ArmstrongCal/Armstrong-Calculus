from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_6_3optsi", 3*width, height)

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
    return 0.2*math.exp(0.9*x) + 0.1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.25,2.75])
graph.draw()

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
    return 0.75*x + 0.2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.25,2.75])
graph.draw()

restore()

save()
margin=10
setupcoordinates([2*width + margin, margin, 3*width-margin, height-margin],
                 [-1, -1, 3, 3])

grid = Grid([-1, 1, 3], [-1, 1, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

def f(x):
    return 2.5 - 2.5*math.exp(-0.9*x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.25,2.75])
graph.draw()

restore()

endfigure()
