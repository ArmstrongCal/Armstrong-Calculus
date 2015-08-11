from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("2_1_Ez3", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3.5, -3.5, 3.5, 3.5])

grid = Grid([-3.5, 0.5, 3.5], [-3.5, 0.5, 3.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([-3,1,3])
axes.drawticks()

axes.setlabels([-3,1,3], # you can do this separately with seth(v)labels
               [-3,1,3])
axes.drawlabels()


label = Label(r"$p$", [-2.75, 3])
label.draw()

label = Label(r"$q$", [-2.75, -2])
label.draw()


def f(x):
    return -2*x-3

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3.5,-1])
graph.draw()

def f(x):
    return 0.5*(x+1)-1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,1])
graph.draw()

def f(x):
    return 2*(x-1)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,3.5])
graph.draw()


def f(x):
    return 3*(x+2)-1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3.5,-1])
graph.draw()

def f(x):
    return 2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,1])
graph.draw()

def f(x):
    return 2 - (x-1)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,3.5])
graph.draw()

restore()

endfigure()
