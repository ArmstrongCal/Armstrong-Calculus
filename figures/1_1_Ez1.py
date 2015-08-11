from figures import *
from defaults import *

width = standardwidth
height = standardheight
beginfigure("1_1_Ez1", width, height)

margin = 10
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-3, -20, 20, 200])


grid = Grid([-3, 1, 20], [-20, 10, 200], color=gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes()
axes.draw()

axes.sethticks([0, 5, 20]) 
axes.setvticks([0, 50, 200])
axes.drawticks()
axes.sethticksize(sizeofaxesticks)
axes.setvticksize(sizeofaxesticks)

axes.setlabels([0, 5, 20],[0, 50, 200])
axes.sethlabelscale(scaleofaxeshlabels)
axes.setvlabelscale(scaleofaxesvlabels)
axes.drawlabels()


label = Label("$s$", [1.1, 180])
label.draw()

label = Label("$t$", [18, 10])
label.draw()



def f(x):
    return 100*(math.cos(.75*x)*math.exp(-0.2*x) + 1)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,20])
graph.setmiterlimit(1)
graph.setN(1000)

graph.draw()

restore()

endfigure()
