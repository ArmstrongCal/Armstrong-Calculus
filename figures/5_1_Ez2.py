from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("5_1_Ez2", 2*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -2.5, 35, 17.5])

grid = Grid([-5, 2.5, 35], [-2.5, 1.25, 17.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 5, 30]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 5, 15])
axes.drawticks()

axes.setlabels([0, 10, 30], # you can do this separately with seth(v)labels
               [0, 5, 15])
axes.drawlabels()

def f(x):
    return 2.5

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,5])
graph.draw()

def f(x):
    return 7.5

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([5,10])
graph.draw()

def f(x):
    return 15

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([10,15])
graph.draw()


def f(x):
    return 12.5

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([15,20])
graph.draw()

def f(x):
    return 10

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([20,25])
graph.draw()

def f(x):
    return 5

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([25,30])
graph.draw()


label = Label("$c$", [20, 12.5], alignment = "lb", offset = [2,2])
label.draw()

label = Label("cal/min", [1, 16], alignment = "lb", offset = [2,2])
label.draw()

label = Label("min", [32, 0.5], alignment = "lb", offset = [2,2])
label.draw()

restore()

###

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-5, -2.5, 35, 17.5])

grid = Grid([-5, 2.5, 35], [-2.5, 1.25, 17.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 5, 30]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 5, 15])
axes.drawticks()

axes.sethlabels([0, 10, 30])
axes.drawhlabels()
restore()

endfigure()
