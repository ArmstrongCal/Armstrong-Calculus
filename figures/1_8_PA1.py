from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_8_PA1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -2, 5, 5])

grid = Grid([-2, 1, 5], [-2, 1, 5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

restore()

endfigure()
