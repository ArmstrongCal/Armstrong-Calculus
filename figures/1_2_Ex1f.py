from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("1_2_Ex1f", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -1, 2, 6])

grid = Grid([-4, 1, 2], [-1, 1, 6])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 1]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 1, 5])
axes.drawticks()

axes.setlabels([-3, 2, 1], # you can do this separately with seth(v)labels
               [1, 2, 5])
axes.drawlabels()


label = Label("$f$", [-3.2, 5.3])
label.draw()


def f(x):
    return 2-x

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,2])
graph.draw()

p1 = Point([-2,4], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

restore()

endfigure()
