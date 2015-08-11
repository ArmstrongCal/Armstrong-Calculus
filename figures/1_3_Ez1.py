from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_3_Ez1", width, height)

save()
margin = 5
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 5, 5])

grid = Grid([-5, 1, 5], [-5, 1, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-4, 2, 4])
axes.setvticks([-4, 2, 4])
axes.drawticks()

axes.setlabels([-4, 4, 4], [-4, 4, 4])
axes.drawlabels()

label = Label("$x$", [4.5, 0.3])
label.draw()

label = Label("$y$", [0.3, 4.5])
label.draw()

label = Label("$f$", [4, 4])
label.draw()

def f(x):
    return 0.1*x*(x+2)*(x-3) + 2

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-5,5])
graph.draw()


restore()

endfigure()
