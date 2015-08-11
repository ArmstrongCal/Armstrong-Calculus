from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("1_1_Ez2b", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -4, 14, 4])


grid = Grid([-2, 1, 14], [-4, 0.5, 4], color=gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 2, 12]) 
axes.setvticks([-3, 1, 3])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.sethlabels([0, 2, 12])
axes.sethlabelscale(scaleofaxeshlabels)
#axes.setvlabelscale(0.8)
axes.drawhlabels()


label = Label("$v$", [0.5, 3.5])
label.draw()

label = Label("$t$", [13, 0.25])
label.draw()


restore()

endfigure()
