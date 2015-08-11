from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_1_Act3Soln", width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -2, 4, 14])

grid = Grid([-4, 1, 4], [-2, 2, 14])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3])
axes.setvticks([0, 2, 12])
axes.drawticks()

axes.setlabels([-2, 4, 2], [0, 4, 12])
axes.drawlabels()

def f(x):
    return x**2 + math.cos(3*x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,4])
graph.draw()

def f(x):
    return x**2 + math.cos(1.6*x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(lightblue)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,4])
graph.draw()


restore()

endfigure()
