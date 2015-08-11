from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("5_6_Act3", 3*width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.25, -0.5, 1.25, 2.5])


grid = Grid([-0.25, 0.25, 1.25], [-0.5, 0.5, 2.5], color=gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 0.25, 1.0]) 
axes.setvticks([0, 0.5, 2.0])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.sethlabels([0, 1, 1])
axes.sethlabelscale(scaleofaxeshlabels)
axes.drawhlabels()

axes.setvlabels([0, 2, 2])
axes.setvlabelscale(scaleofaxeshlabels)
axes.drawvlabels()

restore()

###

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-0.25, -0.5, 1.25, 2.5])


grid = Grid([-0.25, 0.25, 1.25], [-0.5, 0.5, 2.5], color=gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 0.25, 1.0]) 
axes.setvticks([0, 0.5, 2.0])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.sethlabels([0, 1, 1])
axes.sethlabelscale(scaleofaxeshlabels)
axes.drawhlabels()

axes.setvlabels([0, 2, 2])
axes.setvlabelscale(scaleofaxeshlabels)
axes.drawvlabels()


restore()

###

save()
setupcoordinates([2*width+margin, margin, 3*width-margin, height-margin],
                 [-0.25, -0.5, 1.25, 2.5])


grid = Grid([-0.25, 0.25, 1.25], [-0.5, 0.5, 2.5], color=gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 0.25, 1.0]) 
axes.setvticks([0, 0.5, 2.0])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.sethlabels([0, 1, 1])
axes.sethlabelscale(scaleofaxeshlabels)
axes.drawhlabels()

axes.setvlabels([0, 2, 2])
axes.setvlabelscale(scaleofaxeshlabels)
axes.drawvlabels()

restore()


endfigure()
