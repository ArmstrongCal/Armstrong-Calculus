from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("3_1_Act2", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -2, 3, 3])

grid = Grid([-2, 1, 3], [-2, 1, 3])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-1, 1, 2]) 
axes.setvticks([-1, 1, 2])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0, 1, 2],[0, 1, 2])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()


def f(x):
    return -0.25*(x+1)*(x-2)**2

cliptoboundingbox()
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([-2,3])
graph.draw()

label = Label(r"$g''$", [-1.5, f(-1.5)], alignment = "lb", offset = [4,4])
label.draw()

restore()
endfigure()
