from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("5_6_Act2", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.3, -0.3, 2.1, 2.1])


grid = Grid([-0.3, 0.15, 2.1], [-0.3, 0.15, 2.1], color=gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 0.3, 1.8]) 
axes.setvticks([0, 0.3, 1.8])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.sethlabels([0, 0.3, 1.8])
axes.sethlabelscale(scaleofaxeshlabels)
axes.sethlabelscale(0.8)
axes.drawhlabels()

label = Label("$v$", [0.1, 1.9], alignment = "lb", offset = [2,2])
label.draw()

label = Label("$t$", [1.9, 0.1], alignment = "lb", offset = [2,2])
label.draw()


restore()

endfigure()
