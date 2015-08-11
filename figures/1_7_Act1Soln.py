from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_7_Act1Soln", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -2, 3, 4])

grid = Grid([-3, 0.5, 3], [-2, 0.5, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([-2, 1, 4])
axes.drawticks()

axes.setlabels([-3, 1, 3], # you can do this separately with seth(v)labels
               [-2, 1, 4])
axes.sethlabelscale(0.8)
axes.setvlabelscale(0.8)
axes.drawlabels()

label = Label("$x$", [2.5, 0.2])
label.draw()

label = Label("$y$", [0.2, 3.5])
label.draw()


thisgraphwidth = 1.25

def f(x):
    return 3*(x+2)+2

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-3,-2])
graph.draw()

def f(x):
    return 2*(x+2)/3 + 1

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([-2,1])
graph.draw()

def f(x):
    return 4-x

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(thisgraphwidth)
graph.setdomain([1,3])
graph.draw()

p1 = Point([-2,2], 1.5)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-2,1], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()

p1 = Point([-1,1.66667], 1.5)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([1,3], 1.5)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([1,2], 1.5)
p1.setfillcolor(pointcolor)
p1.fill()
p1.draw()


restore()

endfigure()
