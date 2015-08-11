from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_7_PA1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 0.5, 4], [-4, 0.5, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.setlinewidth(1.25)
axes.draw()

axes.sethticks([-3, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-3, 1, 3])
axes.drawticks()

axes.setlabels([-3, 1, 3], # you can do this separately with seth(v)labels
               [-3, 1, 3])
axes.drawlabels()

label = Label("$f$", [-2.8, 3.2])
label.draw()

thisgraphwidth = 1.25

def f(x):
    return 1+2*(x+4)**2

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-4,-3])
graph.draw()

def f(x):
    return 3-(x+3)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-3,-2])
graph.draw()

def f(x):
    return 0.75*x**2-4

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-2,1])
graph.draw()

def f(x):
    return -3.25 + 0.75*(x-1)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([1,2])
graph.draw()

def f(x):
    return -2.5 + math.sin(pi/(x-2))

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([2.002,4])
graph.setmiterlimit(1)
graph.setN(1000)
graph.draw()

p1 = Point([-2,2], 1.5)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-2,-1], 1.5)
p1.setfillcolor(graphcolor)
p1.fill()
p1.draw()

p1 = Point([-1,-3.25], 1.5)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-1,1], 1.5)
p1.setfillcolor(graphcolor)
p1.fill()
p1.draw()

p1 = Point([3,-2.5], 1.5)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()


restore()

endfigure()
