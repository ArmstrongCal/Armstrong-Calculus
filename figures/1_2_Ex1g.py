from figures import *
from defaults import *

width = standardwidth*1.2
height = standardheight*0.6
beginfigure("1_2_Ex1g", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-4, -2, 4, 2])

grid = Grid([-4, 1, 4], [-2, 1, 2])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-3, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 1])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([-3, 2, 3], # you can do this separately with seth(v)labels
               [-2, 2, 2])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label("$g$", [3.2, 1.1])
label.draw()


def f(x):
    return math.sin(pi/x)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setmiterlimit(1)
graph.setlinewidth(graphwidth)
graph.setdomain([-4,-0.01])
graph.setN(6000)
graph.draw()

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setmiterlimit(1)
graph.setlinewidth(graphwidth)
graph.setdomain([0.01,4])
graph.setN(6000)
graph.draw()

restore()

endfigure()
