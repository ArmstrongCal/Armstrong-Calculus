from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_5_PA1", width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-20, -20, 110, 110])

grid = Grid([-20, 10, 110], [-20, 10, 110])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 20, 100])
axes.setvticks([0, 20, 100])
axes.drawticks()
axes.sethticksize(10)

axes.setlabels([20, 20, 100], [20, 20, 100])
axes.drawlabels()

label = Label(r"$t$", [105, 3])
label.draw()

label = Label(r"$s$", [3, 105])
label.draw()

label = Label(r"$(57,63.8)$", [55,65], alignment = "rb", offset = [2, 2])
label.draw()

label = Label(r"$(68,63.8)$", [69,64], alignment = "lt", offset = [-2, -2])
label.draw()

label = Label(r"$(104,106.8)$", [103,107], alignment = "rb", offset = [2, 2])
label.draw()

def f(x):
    return 7*x*x/24

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,2])
graph.draw()

def f(x):
    return 7*(x-2)/6 + 7/6

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2,55.2])
graph.draw()

def f(x):
    return -7*(x-57)*(x-57)/24 + 63.83

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([55.2,57])
graph.draw()


def f(x):
    return 63.83

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([57,66])
graph.draw()

def f(x):
    return 7*(x-66)*(x-66)/24 + 63.83

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([66,68])
graph.draw()

def f(x):
    return 7*(x-68)/6 + 64.83

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([68,104])
graph.draw()

def f(x):
    return -7*(x-106)*(x-106)/24 + 108

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([104,106])
graph.draw()

def f(x):
    return 108

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([106,110])
graph.draw()

p1 = Point([104,106.8], 1)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([57,63.83], 1)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([66,63.83], 1)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

restore()

endfigure()
