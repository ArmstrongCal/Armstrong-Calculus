from figures import *
from defaults import *

width = standardwidth*1.1
height = standardheight

beginfigure("1_2_PA1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2.5, -1.5, 3.5, 4.5])

grid = Grid([-2.5, 0.5, 3.5], [-1.5, 0.5, 4.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2,1,3]) # you can do this in one line with setticks([], [])
axes.setvticks([-1,1,4])
axes.drawticks()

axes.setlabels([-2,1,3], # you can do this separately with seth(v)labels
               [-1,1,3])
axes.drawlabels()

#label = Label("$x$", [3.2, 0.1])
#label.draw()

#label = Label("$y$", [0.1, 4.2])
#label.draw()

label = Label("$g$", [-1.2, 3.2])
label.draw()


def f(x):
    return -(x*x-4)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2.35,1])
graph.draw()

graph.setfunction( Function(lambda x : -x+3))
graph.setdomain([1,3.5])
graph.draw()

p1 = Point([0,4], 2)
p1.setfillcolor(emptypoint)
p1.fill()
p1.draw()

p1.setpoint([1,2])
p1.fill()
p1.draw()

p2 = Point([0,1], 2)
p2.setfillcolor(graphcolor)
p2.fill()
p2.draw()

p2.setpoint([1,3])
p2.fill()
p2.draw()

p3 = Point([2,1], 2)
p3.setfillcolor(emptypoint)
p3.fill()
p3.draw()

restore()

endfigure()
