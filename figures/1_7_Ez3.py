from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_7_Ez3", 2*width, height)

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

axes.setlabels([-3,3,3], # you can do this separately with seth(v)labels
               [-3,3,3])
axes.drawlabels()


restore()

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
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

label = Label("$y=h'(x)$", [1, 1.2])
label.draw()

def f(x):
    return 1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-3.5,-2])
graph.draw()

def f(x):
    return -1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,0])
graph.draw()

def f(x):
    return 1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,2])
graph.draw()

def f(x):
    return -1

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([2,3.5])
graph.draw()

p1 = Point([-2,1], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([-2,-1], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([0,1], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([0,-1], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([2,1], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1 = Point([2,-1], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

restore()

endfigure()
