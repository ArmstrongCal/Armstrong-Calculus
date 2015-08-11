from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_2_Act2", 2*width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-10, -5, 10, 5])

grid = Grid([-10, 1, 10], [-5, 0.5, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()


restore()

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-10, -5, 10, 5])

grid = Grid([-10, 1, 10], [-5, 0.5, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

restore()

endfigure()
