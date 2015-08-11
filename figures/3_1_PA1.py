from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_1_PA1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -3, 3, 3])

grid = Grid([-3, 0.5, 3], [-3, 0.5, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([-2,1,2])
axes.drawticks()

axes.setlabels([-2,1,2], # you can do this separately with seth(v)labels
               [-2,1,2])
axes.drawlabels()

label = Label("$y = h(x)$", [1.1, 2])
label.draw()


def f(x):
    return (2*(x+2.5))**3-2

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3,-2])
graph.draw()

def f(x):
    return -0.5*(x+2)-1

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,0])
graph.draw()

def f(x):
    return -4*(x-1)**2 + 2

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,1.5])
graph.draw()

def f(x):
    return -1*(x-1.5)**2+1

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1.5,3])
graph.draw()

restore()

endfigure()
