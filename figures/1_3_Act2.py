from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("1_3_Act2", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-0.5, -8, 2.5, 40])

xrange = [-0.5,0.5,2.5]
yrange = [-8,8,40]

grid = Grid(xrange, yrange)
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0,0.5,2]) 
axes.setvticks([0,8,32])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0,1,2.5],[0,16,40])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

label = Label("$t$", [2.3, 2])
label.draw()

label = Label("$y$", [0.1, 36])
label.draw()

restore()

endfigure()
