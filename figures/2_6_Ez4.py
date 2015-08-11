from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_6_Ez4", width, height)

margin = 20
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 1, 4], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

label = Label(r"$y = f(x)$", [1,-2])
label.draw()

def f(x):
    return x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(gray)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,4])
graph.draw()

def f(x):
    return 2*math.atan(x-1) - 1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(darkblue)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,4])
graph.draw()

restore()

endfigure()
