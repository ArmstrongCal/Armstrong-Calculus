from figures import *
from defaults import *

width = standardwidth
height = standardheight+30

beginfigure("1_6_PA1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -2, 12, 16])

grid = Grid([-2, 1, 12], [-2, 1, 16])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 2, 10]) 
axes.setvticks([0, 2, 14])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([2, 4, 12],[2, 4, 16])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label("$t$", [11.2, 0.3])
label.draw()

label = Label("$y$", [0.3, 15.2])
label.draw()

label = Label("$s$", [10.2, 15.2])
label.draw()


def f(x):
    return 2*math.sin(0.5*pi*(x-1)) + 2

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,2])
graph.setN(1000)
graph.draw()

def f(x):
    return 4

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2,3])
graph.draw()

def f(x):
    return -2*math.sin(0.5*pi*(x-2)) + 6

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([3,5])
graph.setN(1000)
graph.draw()

def f(x):
    return 8

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([5,7])
graph.draw()

def f(x):
    return -2*math.sin(0.5*pi*(x-2)) + 10

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([7,9])
graph.setN(1000)
graph.draw()

def f(x):
    return 12

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([9,10])
graph.draw()

def f(x):
    return -2*math.sin(0.5*pi*(x-1)) + 14

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([10,12])
graph.setN(1000)
graph.draw()

restore()

endfigure()
