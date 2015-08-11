from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_2_Act3", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1.5, -1.5, 5.5, 5.5])

grid = Grid([-1.5, 0.5, 5.5], [-1.5, 0.5, 5.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 5]) 
axes.setvticks([-1, 1, 5])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([1, 2, 5],[1, 2, 5])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label("$t$", [4.7, 0.3])
label.draw()

label = Label("$s$", [3.8, 4.7])
label.draw()


def f(x):
    return x + 0.5*math.sin(pi*x)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-1.5,5.5])
graph.setN(1000)
graph.draw()

restore()

endfigure()
