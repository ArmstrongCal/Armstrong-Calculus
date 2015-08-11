from figures import *
from defaults import *

width = standardwidth
height = standardheight

beginfigure("5_2_Act2_soln", 2*width, height)

margin = 5
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-10, -1, 10, 1])

grid = Grid([-10, 1, 10], [-1, 0.1, 1])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-5,5,5]) 
axes.setvticks([-0.5,0.5,0.5])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([-0.5,0.5,0.5])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()

axes.sethlabels([-5,5,5])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()

### first original function graph

def f(x):
    return x/(1+x**2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([-9.75, 9.75])
graph.setcolor(darkblue)
graph.draw()

label = Label(r"$f$", [8,0.2], alignment = "lb", offset = [2, 2], scale = 1 )
label.draw()

restore()

###################

save()
setupcoordinates([width+margin, margin, 2*width-margin, height-margin],
                 [-10, -2.5, 10, 2.5])

grid = Grid([-10, 1, 10], [-2.5, 0.25, 2.5])
grid.setcolor(gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([-5,5,5]) 
axes.setvticks([-1.25,1.25,1.25])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setvlabels([-1.25,1.25,1.25])
axes.setvlabelscale(scaleofaxeslabels)
axes.drawvlabels()

axes.sethlabels([-5,5,5])
axes.sethlabelscale(scaleofaxeslabels)
axes.drawhlabels()

### first original function graph

def f(x):
    return 0.5*math.log(1+x**2)

cliptoboundingbox() 
graph = Graph(Function(f))
graph.setdomain([-9.95, 9.95])
graph.setcolor(darkblue)
graph.draw()

label = Label(r"$F$", [8,2], alignment = "lt", offset = [2, -2], scale = 1 )
label.draw()

restore()

endfigure()
