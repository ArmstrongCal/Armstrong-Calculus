from figures import *
from defaults import*

width = 120
height = 180
beginfigure("2_2_PA1a", 2*width, height)

save()
margin = 10
setupcoordinates([margin,margin,width-margin,height-margin], 
                 [-3, -1, 3, 8])

xrange = [-3, 1, 3]
yrange = [-1, 1, 8]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2,1,2]) 
axes.setvticks([0,1,7])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([-2,1,2],[0,1,7])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

### first original function graph

def f(x):
    return 2**x

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.draw()

restore()

### grid for first derivative, second figure

save()
margin = 10
setupcoordinates([width+margin,margin,2*width-margin,height-margin], 
                 [-3, -1, 3, 8])

xrange = [-3, 1, 3]
yrange = [-1, 1, 8]

grid = Grid(xrange, yrange, color = gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-2,1,2]) 
axes.setvticks([0,1,7])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([-2,1,2],[0,1,7])
axes.sethlabelscale(scaleofaxeslabels)
axes.setvlabelscale(scaleofaxeslabels)
axes.drawlabels()

restore()

endfigure()
