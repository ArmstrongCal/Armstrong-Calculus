from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_7_Act1", width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -2, 3, 4])

grid = Grid([-3, 0.5, 3], [-2, 0.5, 4])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2, 1, 2]) # you can do this in one line with setticks([], [])
axes.setvticks([-1, 1, 3])
axes.drawticks()

axes.setlabels([-2, 1, 2], # you can do this separately with seth(v)labels
               [-1, 1, 3])
axes.drawlabels()



thisgraphwidth = 1.25



restore()

endfigure()
