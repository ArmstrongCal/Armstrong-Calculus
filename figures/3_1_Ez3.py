from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_1_Ez3", width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -4, 4, 4])

grid = Grid([-4, 1, 4], [-4, 1, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3])
axes.setvticks([-3, 1, 3])
axes.drawticks()

axes.setlabels([0, 4, 2], [0, 4, 2])
axes.drawlabels()

def f(x):
    return 6/pi*math.atan(2*x)

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,4])
graph.draw()

label = Label("$h'$", [2,2.8])
label.draw()

restore()

endfigure()
