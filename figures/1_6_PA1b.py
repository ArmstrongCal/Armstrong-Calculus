from figures import *
from defaults import *

width = standardwidth
height = standardheight+30

beginfigure("1_6_PA1b", 2*width, height)

save()
margin = 10
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-2, -8, 12, 8])

grid = Grid([-2, 1, 12], [-8, 1, 8])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 2, 10]) 
axes.setvticks([-6, 2, 6])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.sethlabels([2, 4, 12])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()

label = Label("$t$", [11.2, 0.3])
label.draw()

label = Label("$y$", [0.3, 7.2])
label.draw()

#label = Label("$s$", [4.5, 4.7])
#label.draw()

restore()

save()
margin = 10
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-2, -8, 12, 8])

grid = Grid([-2, 1, 12], [-8, 1, 8])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 2, 10]) 
axes.setvticks([-6, 2, 6])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.sethlabels([2, 4, 12])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()

label = Label("$t$", [11.2, 0.3])
label.draw()

label = Label("$y$", [0.3, 7.2])
label.draw()

#label = Label("$s$", [4.5, 4.7])
#label.draw()

restore()

endfigure()
