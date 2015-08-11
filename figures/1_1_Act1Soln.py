from figures import *
from defaults import *

width = standardwidth*0.8
height = standardheight*1.2
beginfigure("1_1_Act1Soln", width, height)

margin = 15
save()
setupcoordinates([margin, margin, width-margin, height-margin],
                 [0, 44, 1.22, 68])

grid = Grid([0, 0.2, 1.22], [44, 2, 68], color=gridcolor)
grid.setlinewidth(gridwidth)
grid.draw()

axes = Axes(labelalignment="lb", frame = "lb")
axes.draw()

axes.sethticks([0, 0.4, 1.22])
axes.setvticks([44,4,68])
axes.drawticks()
##axes.sethticksize(10)
##axes.setvticksize(10)

axes.setlabels([0.4, 0.4, 1.22],[48,8,68])
axes.sethlabelscale(scaleofaxeshlabels)
axes.setvlabelscale(scaleofaxesvlabels)
axes.drawlabels()

label = Label("feet", [0.06, 66])
label.draw()

label = Label("sec", [1.0, 45])
label.draw()

label = Label("$s$", [1.1, 64.5])
label.draw()

label = Label("$A$", [0.43, 57.5])
label.draw()

label = Label("$B$", [0.83, 62])
label.draw()

def f(x):
    return 64-16*(x-1)*(x-1)

graph = Graph(Function(f))
graph.setcolor(graphcolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0,1.2])
graph.draw()

def g(x):
    return f(0.4) + (f(0.8)-f(0.4))/(0.8-0.4)*(x-0.4)

graph = Graph(Function(g))
graph.setcolor(tangentlinecolor)
graph.setlinewidth(graphwidth)
graph.setdomain([0.2,1.0])
graph.draw()

point = Point([0.4, f(0.4)], size = 2, fillcolor=pointcolor)
point.fill()
point.draw()

point = Point([0.8, f(0.8)], size = 2, fillcolor=pointcolor)
point.fill()
point.draw()

restore()

endfigure()
