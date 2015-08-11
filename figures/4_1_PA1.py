from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("4_1_PA1", 2*width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.25, -1, 2.5, 9])

grid = Grid([-0.25, 0.25, 2.5], [-1, 1, 9])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([0,2,8])
axes.drawticks()

axes.setlabels([0,1,2], # you can do this separately with seth(v)labels
               [0,4,8])
axes.drawlabels()

label = Label("mph", [0.1,8], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2.1,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-0.25, -1, 2.5, 9])

grid = Grid([-0.25, 0.25, 2.5], [-1, 1, 9])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,1,2]) # you can do this in one line with setticks([], [])
axes.setvticks([0,2,8])
axes.drawticks()

axes.setlabels([0,1,2], # you can do this separately with seth(v)labels
               [0,4,8])
axes.drawlabels()

label = Label("miles", [0.1,8], alignment = "lb", offset = [2, 2] )
label.draw()

label = Label("hrs", [2.1,0.25], alignment = "lb", offset = [2, 2] )
label.draw()

restore()

endfigure()
