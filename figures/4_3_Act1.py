from figures import *
from defaults import *

width = standardwidth*1.6
height = standardheight*0.8

beginfigure("4_3_Act1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3.5, -2, 4.5, 2])

grid = Grid([-3.5, 0.5, 4.5], [-2, 0.5, 2])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3,1,4]) # you can do this in one line with setticks([], [])
axes.setvticks([-1,1,1])
axes.drawticks()

axes.setlabels([-3,1,4], # you can do this separately with seth(v)labels
               [-1,1,1])
axes.drawlabels()

#label = Label("$x$", [3.2, 0.1])
#label.draw()

#label = Label("$y$", [0.1, 4.2])
#label.draw()

label = Label("$g$", [-1.2, 3.2])
label.draw()

def f(x):
    return x+3

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3,-2])
graph.draw()

def f(x):
    return math.sqrt(1-(x+2)**2)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,-1.001])
graph.draw()

def f(x):
    return -1-x

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,0])
graph.draw()

def f(x):
    return -1

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,1])
graph.draw()

def f(x):
    return x-2

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,2])
graph.draw()

def f(x):
    return math.sqrt(1-(x-3)**2)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2.001,3.999])
graph.draw()


label = Label(r"$y = g(x)$", [3,1], alignment = "rb", offset = [-2, 2] )
label.draw()

restore()

endfigure()
