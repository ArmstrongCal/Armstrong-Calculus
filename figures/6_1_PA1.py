from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("6_1_PA1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -1, 4, 8])

grid = Grid([-0.5, 0.5, 4], [-1, 1, 8])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 1, 3]) # you can do this in one line with setticks([], [])
axes.setvticks([0, 2, 6])
axes.drawticks()

axes.setlabels([0, 1, 3], # you can do this separately with seth(v)labels
               [0, 2, 6])
axes.drawlabels()




restore()

endfigure()
