from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_7_NoLimit", 2*width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1, -1, 4, 4])

grid = Grid([-1, 1, 4], [-1, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([2, 1, 3])
axes.drawticks()

axes.setlabels([1,3,2], # you can do this separately with seth(v)labels
               [2,1,3])
axes.drawlabels()

def f(x):
    return 0.5*x+1.5

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,1])
graph.draw()

def f(x):
    return 3.5-0.5*x

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1,4])
graph.draw()

p1 = Point([1,2], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([1,3], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

label = Label("$f$", [1.3, 3.1])
label.draw()

restore()

save()
margin = 10
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-1, -1, 4, 4])

grid = Grid([-1, 1, 4], [-1, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([1, 3, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([1, 1, 3])
axes.drawticks()

axes.setlabels([1,3,3], # you can do this separately with seth(v)labels
               [1,1,3])
axes.drawlabels()


def f(x):
    return 0.5*x+1.5

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1,1])
graph.draw()

def f(x):
    return math.sin(pi/(x-1))+2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([1.001,4])
graph.setmiterlimit(1)
graph.setN(3000)
graph.draw()

label = Label("$g$", [2.5, 3.1])
label.draw()


restore()

endfigure()
