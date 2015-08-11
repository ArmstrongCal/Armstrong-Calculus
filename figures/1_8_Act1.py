from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_8_Act1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-5, -5, 2, 2])

grid = Grid([-5, 1, 2], [-5, 1, 2])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

restore()

endfigure()
